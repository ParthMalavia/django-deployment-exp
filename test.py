from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TAMPLATES_DIR = Path.joinpath(BASE_DIR, "template")
print(TAMPLATES_DIR)