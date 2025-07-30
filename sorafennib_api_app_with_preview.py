from fastapi import FastAPI, Query
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from typing import Optional
import matplotlib.pyplot as plt
import numpy as np
import base64
import io
import os

try:
    from rdkit import Chem
    from rdkit.Chem import Draw
except ImportError:
    Draw = None

app = FastAPI(title="Aspirin Visualizer API", description="Render attention map or molecule from SMILES", version="1.1")

class AttentionParams(BaseModel):
    width: int = Query(10, description="Width of attention map")
    height: int = Query(10, description="Height of attention map")
    border_thickness: float = Query(0.1, description="Border padding in inches")
    seed: int = Query(0, description="Random seed")
    transparent: Optional[bool] = Query(False, description="Transparent background")
    multi: Optional[bool] = Query(False, description="Multi-color attention view")

def image_to_base64(fig) -> str:
    buf = io.BytesIO()
    fig.savefig(buf, format='png', bbox_inches='tight')
    plt.close(fig)
    buf.seek(0)
    return base64.b64encode(buf.read()).decode("utf-8")

@app.get("/plot_attention")
def plot_attention(params: AttentionParams):
    np.random.seed(params.seed)
    data = np.random.rand(params.height, params.width)
    fig, ax = plt.subplots(figsize=(params.width, params.height))
    cax = ax.matshow(data, cmap='viridis')
    for (i, j), val in np.ndenumerate(data):
        ax.text(j, i, f'{val:.2f}', ha='center', va='center', color='white')
    plt.colorbar(cax)
    plt.title("Attention Map")
    img_b64 = image_to_base64(fig)
    return JSONResponse(content={"preview": f"data:image/png;base64,{img_b64}"})

@app.get("/render_smiles")
def render_smiles(smiles: str = Query(..., description="SMILES string")):
    if Draw is None:
        return {"error": "RDKit not installed"}
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return {"error": "Invalid SMILES string"}
    img = Draw.MolToImage(mol, size=(300, 300))
    buf = io.BytesIO()
    img.save(buf, format='PNG')
    img_b64 = base64.b64encode(buf.getvalue()).decode("utf-8")
    return JSONResponse(content={"preview": f"data:image/png;base64,{img_b64}"})
