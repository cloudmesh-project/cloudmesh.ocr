This directory contains two playbooks along with all the roles for deploying the project on Chameleon Cloud.

deploy_stack playbook runs:
- Installs Git, OpenCV
- Fetches Python codes of OCR.
- Fetches the dataset on which OCR runs.

run_ocr playbook runs:
- Runs the Python codes.
- Fetches the resulting files from the remote VMs.
