# 1. Install (if you haven't yet)
pip install --upgrade "huggingface_hub[cli]"

# 2. Full download
hf download InternRobotics/OmniWorld \
           --repo-type dataset \
           --local-dir /path/to/DATA_PATH