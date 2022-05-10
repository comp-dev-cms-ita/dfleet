# Copyright (c) 2022 dciangot
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import requests
import dfleet.identity as identity
import json

# JLab extension api ref: https://github.com/comp-dev-cms-ita/dask-labextension/blob/af_plugin/dask_labextension/__init__.py#L57


def generate_dashboard_url(cluster_id: str, name: str, jhub_url: str) -> str:
    return f"{jhub_url}/user/{name}/dask/dashboard/{cluster_id}/status"


def create(token: str, jhub_url: str, sitename: str = "HTCondor-T2_LNL_PD", adapt: dict = {"minimum": 10, "maximum": 50}, verbose: bool = False) -> dict :
    headers = {'Authorization': f'token {token}'}
    if verbose:
        print(headers)

    try:
        id_dict = identity.whoami(token=token, jhub_url=jhub_url, verbose=verbose) 
    except Exception as ex:
        raise ex

    url = jhub_url + f"/user/{id_dict['name']}/dask/clusters/"

    if verbose:
        print(sitename)
        print(url)
        print(adapt)

    try:
        r = requests.put(url, data=json.dumps({'factoryName': sitename, "adapt": adapt}), headers=headers)
    except Exception as ex:
        raise ex

    r_enriched = r.json()

    r_enriched['dashboard_url'] = generate_dashboard_url(
        name=id_dict['name'],
        cluster_id=r_enriched['id'],
        jhub_url=jhub_url
    )

    return r_enriched


def status(token: str, jhub_url: str, cluster_id: str, verbose: bool = False) -> dict:
    try:
        id_dict = identity.whoami(token=token, jhub_url=jhub_url, verbose=verbose) 
    except Exception as ex:
        raise ex
    
    url = jhub_url + f"/user/{id_dict['name']}/dask/clusters/{cluster_id}"

    headers = {'Authorization': f'token {token}'}
    if verbose:
        print(headers)

    try:
        r = requests.get(url, headers=headers)
    except Exception as ex:
        raise ex

    r_enriched = r.json()

    r_enriched['dashboard_url'] = generate_dashboard_url(
        name=id_dict['name'],
        cluster_id=r_enriched['id'],
        jhub_url=jhub_url
    )

    return r_enriched


def list(token: str, jhub_url: str, verbose: bool = False) -> dict:
    try:
        id_dict = identity.whoami(token=token, jhub_url=jhub_url, verbose=verbose) 
    except Exception as ex:
        raise ex
    
    url = jhub_url + f"/user/{id_dict['name']}/dask/clusters/"

    headers = {'Authorization': f'token {token}'}
    if verbose:
        print(headers)

    try:
        r = requests.get(url, headers=headers)
    except Exception as ex:
        raise ex

    return r.json()


def delete(token: str, jhub_url: str, cluster_id: str, verbose: bool = False) -> None:
    try:
        id_dict = identity.whoami(token=token, jhub_url=jhub_url, verbose=verbose) 
    except Exception as ex:
        raise ex

    url = jhub_url + f"/user/{id_dict['name']}/dask/clusters/{cluster_id}"

    headers = {'Authorization': f'token {token}'}
    if verbose:
        print(headers)

    try:
        requests.delete(url, headers=headers)
    except Exception as ex:
        raise ex

    return


def edit(token: str, jhub_url: str, cluster_id: str, adapt: dict = None, workers: int = None, verbose: bool = False) -> dict:
    headers = {'Authorization': f'token {token}'}
    if verbose:
        print(headers)

    try:
        id_dict = identity.whoami(token=token, jhub_url=jhub_url, verbose=verbose) 
    except Exception as ex:
        raise ex

    url = jhub_url + f"/user/{id_dict['name']}/dask/clusters/{cluster_id}"

    if verbose:
        print(url)
        print(adapt)

    print(adapt)
    print(workers)
    if adapt:
        try:
            r = requests.patch(url, data=json.dumps({"adapt": adapt}), headers=headers)
        except Exception as ex:
            raise ex
    else:
        try:
            r = requests.patch(url, data=json.dumps({"workers": workers}), headers=headers)
        except Exception as ex:
            raise ex 

    r_enriched = r.json()

    r_enriched['dashboard_url'] = generate_dashboard_url(
        name=id_dict['name'],
        cluster_id=r_enriched['id'],
        jhub_url=jhub_url
    )

    return r_enriched
