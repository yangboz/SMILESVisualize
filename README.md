# Attention Map and SMILES Renderer

This Python utility supports two modes:
1. Generating attention maps using random data.
2. Rendering molecular structures from SMILES strings using RDKit.

## Requirements

- `matplotlib`
- `numpy`
- (Optional for SMILES) `rdkit`

Install RDKit via conda:
```bash
conda install -c rdkit rdkit
```

---

## Usage

### 1. Generate Random Attention Map

**Basic PNG output:**

```bash
python sorafennib_attention_plot_with_smiles.py --width 12 --height 8 --output result.png
```

**Multi colormap + PDF output + transparent background:**

```bash
python sorafennib_attention_plot_with_smiles.py --multi --transparent --output result.pdf
```

### 2. Render Molecule from SMILES

```bash
python sorafennib_attention_plot_with_smiles.py --smiles "CC(=O)OC1=CC=CC=C1C(=O)O" --output aspirin.png
```

---

## Parameters

| Argument             | Description                                                  | Default       |
|----------------------|--------------------------------------------------------------|---------------|
| `--width`            | Width of attention map (columns)                             | `10`          |
| `--height`           | Height of attention map (rows)                               | `10`          |
| `--border-thickness`| Padding for output image in inches                            | `0.1`         |
| `--seed`             | Random seed for data generation                              | `0`           |
| `--output`           | Output file path (`.png` or `.pdf`)                          | `attention_map.png` |
| `--transparent`      | Save image with transparent background                        | *(off)*       |
| `--multi`            | Plot three subplots using different colormaps                | *(off)*       |
| `--smiles`           | SMILES string for molecule rendering (takes precedence)      | `""`          |

---

## Examples

Render aspirin molecule:

![vitamin](https://github.com/yangboz/SMILESVisualize/blob/master/SMILES_vitamin.jpeg)
```bash
python sorafennib_attention_plot_with_smiles.py --smiles "CC(=O)OC1=CC=CC=C1C(=O)O" --output aspirin.png
```

Random attention map, multi-color, saved as PDF:
```bash
python sorafennib_attention_plot_with_smiles.py --multi --output map.pdf
```


# SMILES need colorful visualization?
 oe with a python fastapi   restful template for sharing simplified Molecular input line entry system.

  ## examples: 

  
### SMILE text: Thiamine (vitamin B1, C12H17N4OS+)

Molecular structure of thiamin	OCCc1c(C)[n+](cs1)Cc2cnc(C)nc2N

### visualize:

![vitamin](https://github.com/yangboz/SMILESVisualize/blob/master/SMILES_vitamin.jpeg)

## how to verify it?
```
pip install -r requirements.txt

```

## quick start


```
uvicorn application.server.main:app
```
then check http://localhost:8000/docs#
# docker

```
docker run -p 80:80 smartkit/fastapi-restful-starter
```

###SMILES

https://en.wikipedia.org/wiki/Simplified_Molecular_Input_Line_Entry_System

### need more complex,high resolution ?

drop email to youngwelle@gmail.com
