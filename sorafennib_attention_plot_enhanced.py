import matplotlib.pyplot as plt
import numpy as np
import argparse
import os

def plot_attention_map(width, height, border_thickness, seed, output, transparent, multi):
    np.random.seed(seed)
    data = np.random.rand(height, width)

    if multi:
        fig, axs = plt.subplots(1, 3, figsize=(width * 3, height))
        cmaps = ['viridis', 'plasma', 'cividis']
        for ax, cmap in zip(axs, cmaps):
            cax = ax.matshow(data, cmap=cmap)
            for (i, j), val in np.ndenumerate(data):
                ax.text(j, i, f'{val:.2f}', ha='center', va='center', color='white')
            ax.set_title(f"Cmap: {cmap}")
        fig.colorbar(cax, ax=axs.ravel().tolist())
    else:
        fig, ax = plt.subplots(figsize=(width, height))
        cax = ax.matshow(data, cmap='viridis')
        for (i, j), val in np.ndenumerate(data):
            ax.text(j, i, f'{val:.2f}', ha='center', va='center', color='white')
        plt.colorbar(cax)
        plt.title("Attention Map")

    output_ext = os.path.splitext(output)[-1].lower()
    if output_ext not in ['.png', '.pdf']:
        raise ValueError("Output file must end with .png or .pdf")

    plt.savefig(output, bbox_inches='tight', pad_inches=border_thickness, transparent=transparent)
    print(f"Saved attention map to {output}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate attention map with configurable settings.")
    parser.add_argument('--width', type=int, default=10, help='Number of columns in the attention map (default: 10)')
    parser.add_argument('--height', type=int, default=10, help='Number of rows in the attention map (default: 10)')
    parser.add_argument('--border-thickness', type=float, default=0.1, help='Thickness of border padding in inches (default: 0.1)')
    parser.add_argument('--seed', type=int, default=0, help='Random seed for generating data (default: 0)')
    parser.add_argument('--output', type=str, default='attention_map.png', help='Output file name with extension (.png or .pdf)')
    parser.add_argument('--transparent', action='store_true', help='Make background transparent')
    parser.add_argument('--multi', action='store_true', help='Generate multi-subplot version with different colormaps')

    args = parser.parse_args()
    plot_attention_map(args.width, args.height, args.border_thickness, args.seed, args.output, args.transparent, args.multi)
