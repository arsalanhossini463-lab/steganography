# Image Steganography with Streamlit

A small collection of Streamlit apps that hide secret data inside images using **LSB (Least Significant Bit) steganography**, built with the [`stegano`](https://pypi.org/project/stegano/) library and Pillow.

You can hide a text message or even another picture inside a cover image, and later reveal it again from the generated PNG. The result looks identical to the original image to the human eye.

## Features

- Hide a secret **text** inside an image and reveal it later
- Hide a secret **image** inside another image and recover it
- Simple web interface powered by Streamlit (sidebar to switch between *Hide* and *Reveal* modes)
- Supports `PNG` and `JPG` as input images

## Project Structure

```
.
├── app_1.py            # Hide / reveal text in an image (main text app)
├── app_2.py            # Hide / reveal a picture inside another picture
├── app_3.py            # Simplified text version (early draft of app_1)
├── requirements.txt    # Python dependencies
└── README.md
```

| File | Description |
|------|-------------|
| `app_1.py` | Hide text in an image with a **Hide** button and reveal it with a **Reveal** button. Saves the result as `final_img_pars.png`. |
| `app_2.py` | Hide a secret image inside a cover image. The secret image bytes are encoded as text (`latin-1`) and embedded with LSB. Saves the result as `final_img_2027.png` and restores the secret image as `Gust_pic.jpg`. |
| `app_3.py` | A simplified version of the text app without the extra buttons. |

## Requirements

- Python 3.8+
- The packages listed in `requirements.txt` (`streamlit`, `stegano`, `Pillow`)

## Installation

```bash
# 1. Clone the repository
git clone https://github.com/arsalanhossini463-lab/image-steganography-streamlit.git
cd image-steganography-streamlit

# 2. (Optional but recommended) create a virtual environment
python -m venv venv

# Windows
venv\Scripts\activate
# Linux / macOS
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
```

## Usage

Run any of the apps with Streamlit:

```bash
streamlit run app_1.py
```

Then open the local URL shown in the terminal (usually `http://localhost:8501`).

### Hide text (`app_1.py`)

1. Choose **Hide Text** from the sidebar.
2. Upload a host image (`png` or `jpg`).
3. Type the text you want to hide.
4. Click **Hide**. The output is saved as `final_img_pars.png`.

### Reveal text (`app_1.py`)

1. Choose **Reveal Text** from the sidebar.
2. Upload the generated `PNG` image.
3. Click **Reveal:** to display the hidden message.

### Hide a picture in a picture (`app_2.py`)

```bash
streamlit run app_2.py
```

1. Choose **Hide Picture** and upload a host image and a secret image.
2. Click **Hide Pic**. The result is saved as `final_img_2027.png`.
3. To recover it, choose **Reveal Picture**, upload the generated PNG, and click **Reveal Pic**.

## Important Notes

- **Always share the result as PNG.** PNG is lossless. Saving or converting to JPG (or sending the image through apps that recompress it) destroys the hidden data.
- **Capacity is limited.** The secret must fit inside the host image. For picture-in-picture hiding, use a small secret image and a much larger host image.
- Output files are saved in the folder where you run the app and will overwrite files with the same name.

## How It Works

LSB steganography replaces the least significant bit of each pixel's color values with bits of the secret message. Since this changes each color value by at most 1, the difference is invisible to the human eye, but the message can be read back by extracting those bits in order.

## Built With

- [Streamlit](https://streamlit.io/)
- [Stegano](https://pypi.org/project/stegano/)
- [Pillow](https://python-pillow.org/)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

Created by [arsalanhossini463-lab](https://github.com/arsalanhossini463-lab).
