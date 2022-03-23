# Copyright (c) 2022 dciangot
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import requests


def whoami(token: str, jhub_url: str, verbose: bool = False) -> dict:
    headers = {'Authorization': f'token {token}'}
    if verbose:
        print(headers)

    path = f"/hub/api/authorizations/token/{token}"

    url = jhub_url + path

    if verbose:
        print(f"{url}")

    try:
        r = requests.get(url, headers=headers)
    except Exception as ex:
        raise ex
    
    if verbose:
        print(f"{r.json()}")

    return r.json()

