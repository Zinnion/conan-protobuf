## Package Status

## protobuf / proto v3

Zinnion packages can be found in the following public Conan repository:

[Zinnion Public Conan Repository on Bintray](https://bintray.com/zinnion/cpp/protobuf%3Amaurodelazeri)

```
cd test_package
protoc addressbook.proto --cpp_out=.
```

conan create . maurodelazeri/stable --build missing
