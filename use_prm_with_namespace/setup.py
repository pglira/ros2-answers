import os
from glob import glob

from setuptools import setup

package_name = "use_prm_with_namespace"

setup(
    name=package_name,
    version="0.0.0",
    packages=[package_name],
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
        (os.path.join("share", package_name), glob("launch/*_launch.py")),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="vscode",
    maintainer_email="philipp.glira@ait.ac.at",
    description="TODO: Package description",
    license="TODO: License declaration",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "use_prm_with_namespace = use_prm_with_namespace.use_prm_with_namespace:main"
        ],
    },
)
