# manga_translator

## 1. Installation

<a name="11-install-paddlepaddle"></a>

### 1.1 Install PaddlePaddle

> If you do not have a Python environment, please refer to [Environment Preparation](./environment_en.md).

- If you have CUDA 9 or CUDA 10 installed on your machine, please run the following command to install

  ```bash
  python3 -m pip install paddlepaddle-gpu
  ```

- If you have no available GPU on your machine, please run the following command to install the CPU version

  ```bash
  python3 -m pip install paddlepaddle
  ```

For more software version requirements, please refer to the instructions in [Installation Document](https://www.paddlepaddle.org.cn/install/quick) for operation.

<a name="12-install-paddleocr-whl-package"></a>

### 1.2 Install PaddleOCR Whl Package

```bash
pip install "paddleocr>=2.0.1" # Recommend to use version 2.0.1+
```

- **For windows users:** If you getting this error `OSError: [WinError 126] The specified module could not be found` when you install shapely on windows. Please try to download Shapely whl file [here](http://www.lfd.uci.edu/~gohlke/pythonlibs/#shapely).

  Reference: [Solve shapely installation on windows](https://stackoverflow.com/questions/44398265/install-shapely-oserror-winerror-126-the-specified-module-could-not-be-found)

- **For layout analysis users**, run the following command to install **Layout-Parser**

  ```bash
  pip3 install -U https://paddleocr.bj.bcebos.com/whl/layoutparser-0.0.0-py3-none-any.whl
  ```

<a name="2-easy-to-use"></a>
