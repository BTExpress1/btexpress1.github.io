from PIL import Image, ImageOps

# Configuration
input_path = "assets/images/logo.png"
output_path = "assets/images/favicon.png"
bg_color = "#1a1a1a"  # Matches your navbar charcoal
size = (32, 32)

def generate_favicon():
    # Open original logo
    img = Image.open(input_path).convert("RGBA")

    # Create dark background square
    favicon = Image.new("RGBA", size, bg_color)

    # Calculate padding so logo doesn't touch the edges
    padding = 4
    inner_size = (size[0] - padding, size[1] - padding)

    # Resize logo and center it
    img.thumbnail(inner_size, Image.Resampling.LANCZOS)

    # Paste logo onto background
    offset = ((size[0] - img.width) // 2, (size[1] - img.height) // 2)
    favicon.paste(img, offset, img)

    # Save
    favicon.save(output_path, "PNG")
    print(f"✓ Favicon created at {output_path}")

if __name__ == "__main__":
    generate_favicon()