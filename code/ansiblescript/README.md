This directory contains three playbooks along with all the roles for deploying the project on Chameleon Cloud.

deploy_stack playbook:
- Installs Git, OpenCV
- Fetches Python codes of OCR.
- Fetches the dataset on which OCR runs.

benchmark playbook:
- Runs the Python codes for benchmarking the accuracy of the algorithm on Chars74k dataset. It also fetches the resulting files from the remote VMs.

ocr playbook:
- Runs the OCR algorithm on an image file from the web.
