#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from conans import ConanFile, CMake


class TestPackageConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.definitions["protobuf_VERBOSE"] = True
        cmake.definitions["protobuf_MODULE_COMPATIBLE"] = True
        cmake.configure()
        cmake.build()

    def test(self):
        self.run("protoc --version", run_environment=True)
        bin_path = os.path.abspath(os.path.join("bin", "test_package"))
        self.run(bin_path, run_environment=True)
