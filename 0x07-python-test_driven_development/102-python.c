#include <stdio.h>
#include <string.h>
#include <Python.h>

/**
 * print_python_string - Prints string information
 *
 * @p: Python Object
 * Return: no return
 */
void print_python_string(PyObject *p)
{
    PyObject *str, *repr;
    repr = PyObject_Repr(p);
    str = PyUnicode_AsEncodedString(p, "utf-8", "~E~");

    printf("[.] string object info\n");

    if (strcmp(p->ob_type->tp_name, "str") != 0)
    {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    printf("  type: %s\n", PyUnicode_IS_COMPACT_ASCII(p) ? "compact ascii" : "compact unicode object");
    printf("  length: %ld\n", PyUnicode_GET_SIZE(p));
    printf("  value: %s\n", PyBytes_AsString(str));

    Py_XDECREF(str);
    Py_XDECREF(repr);
}
