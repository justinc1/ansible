# -----------------------------------------
# injected_into_main.py
import os
import vcr
from ansible.module_utils.urls import Request


def injected_into_main():
    print("In injected_into_main")
    with open("/tmp/aa", "a") as ff:
        ff.write("test in injected_into_main\n")

    # with vcr.use_cassette('synopsis.yaml') as cass:
    #     request = Request()
    #     request.get('http://www.zombo.com/')


def main():

    my_vcr = vcr.VCR(
        serializer='json',
        cassette_library_dir='/tmp',
        record_mode='all',
        match_on=['uri', 'method'],
    )
    cassette = vcr.use_cassette('ansible.yaml')
    with cassette:
        # request = Request()
        # request.get('http://ifconfig.me')
        return main_renamed()


if os.environ.get("TEST_INJECT") == "1":
    injected_into_main()
# -----------------------------------------
