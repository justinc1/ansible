export SC_HOST=https://10.5.11.50
export SC_USERNAME=xlab
#export SC_PASSWORD=...
# ansible-galaxy collection install scale_computing.hypercore
# ansible-playbook hc3_api.yml


source .venv/bin/activate
pip install -U pip
(cd hhelper && pip install -e .)

pip install vcrpy
