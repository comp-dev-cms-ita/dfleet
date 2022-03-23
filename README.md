# dfleet

a CLI to mange fleets of remote Dask clusters via JLab Dask extension

## Requirements

- go to https://cms-it-hub.cloud.cnaf.infn.it/hub/token and get one token

- use the token as password to connect to your on-demand UI via:

```bash
ssh <username>@cms-it-hub.cloud.cnaf.infn.it -p 32022
```

## Install

- Install via pip
```bash
pip install git+https://github.com/comp-dev-cms-ita/dfleet
```

- Setup the environment

```bash
# you do NOT need to set JUPYTERHUB_API_TOKEN  if you sit on a jlab instance
# this is only needed if you are running the CLI from your laptop
export JUPYTERHUB_API_TOKEN=<PUT JHUB TOKEN HERE>


export JUPYTERHUB_HOST=https://cms-it-hub.cloud.cnaf.infn.it
```

## Create a cluster

```bash
dfleet  cluster create --sitename HTCondor-T2_LNL_PD_CloudVeneto
```

For more options:
```bash
dfleet  cluster create --help
```

## Delete a cluster

```bash
dfleet cluster delete <PUT CLUSTER ID HERE>
```

## List created clusters

```bash
dfleet cluster list
```
