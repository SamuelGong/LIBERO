# read the contents of your README file
from os import path

from setuptools import find_packages, setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "./README.md"), encoding="utf-8") as f:
    lines = f.readlines()

# remove images from README
lines = [x for x in lines if ".png" not in x]
long_description = "".join(lines)

setup(
    name="libero",
    packages=[package for package in find_packages() if package.startswith("libero")],
    install_requires=[],
    eager_resources=["*"],
    include_package_data=True,
    python_requires=">=3",
    description="LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning",
    author="Bo Liu, Yifeng Zhu, Chongkai Gao, Yihao Feng, Qiang Liu, Yuke Zhu, Peter Stone",
    # url="https://github.com/ARISE-Initiative/robosuite",
    author_email="bliu@cs.utexas.edu, yifengz@cs.utexas.edu",
    version="0.1.0",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_data={
            # 这里的 key 要写“包含 init_files 的那个 package 名字”
            # 你的路径是 site-packages/libero/libero/init_files
            # 一般对应包名就是 "libero.libero"
            "libero.libero": [
                "init_files/*",
                "init_files/*/*",      # 一层子目录
                "init_files/*/*/*",    # 再多一层（保险一点）
                "bddl_files/*",
                "bddl_files/*/*",      # 一层子目录
                "bddl_files/*/*/*",    # 再多一层（保险一点）
            ],
        },
    entry_points={
        "console_scripts": [
            "lifelong.main=libero.lifelong.main:main",
            "lifelong.eval=libero.lifelong.evaluate:main",
            "libero.config_copy=scripts.config_copy:main",
            "libero.create_template=scripts.create_template:main",
        ]
    },
)
