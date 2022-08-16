<h1 align="center">octomap-python</h1>
<h4 align="center">Python binding of <a href="https://github.com/OctoMap/octomap">the OctoMap library</a>.</h4>

<div align="center">
  <a href="https://pypi.python.org/pypi/octomap-python"><img src="https://img.shields.io/pypi/v/octomap-python.svg"></a>
  <a href="https://pypi.org/project/octomap-python"><img src="https://img.shields.io/pypi/pyversions/octomap-python.svg"></a>
  <a href="https://github.com/wkentaro/octomap-python/actions"><img src="https://github.com/wkentaro/octomap-python/workflows/ci/badge.svg"></a>
</div>


## Installation

```bash
pip install octomap-python
```


## Example

```bash
git clone --recursive https://github.com/wkentaro/octomap-python.git && cd octomap-python
pip install -e '.[example]'

cd examples
python insertPointCloud.py
```

<img src="examples/.readme/insertPointCloud.jpg" height="200px" />


## Acknowledgement

This is a fork of [neka-nat/python-octomap](https://github.com/neka-nat/python-octomap).



## STEPS:
RUN in same terminal:
1.  At root run : python setup.py bdist_wheel
2.  Set LD_LIBRARY_PATH : export LD_LIBRARY_PATH=/home/gsuveer/octomap/lib
        Install from  : https://github.com/suveergarg/octomap/tree/gsuveer/semantic_octomap
3.  cd dist/
      There should be a .whl file here.
4.  auditwheel repair --plat manylinux_2_31_x86_64 octomap_python-1.8.0.post12-cp38-cp38-linux_x86_64.whl
      This will create a folder called wheelhouse with the final .whl file.
5.  install this FINAL .whl file using : 
    pip install <path to octomap-python>/dist/wheelhouse/octomap_python-1.8.0.post12-cp38-cp38-manylinux_2_31_x86_64.whl --force-reinstall
6.  Resinstall right version of numpy: pip install numpy==1.22.4 --force-reinstall