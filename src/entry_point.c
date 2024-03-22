#include <Python.h>

static PyMethodDef module_methods[] = {
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef module_definition = {
    PyModuleDef_HEAD_INIT,
    "solidity",
    NULL,
    -1,
    module_methods
};

PyMODINIT_FUNC PyInit_solidity(void) {
    return PyModule_Create(&module_definition);
}
