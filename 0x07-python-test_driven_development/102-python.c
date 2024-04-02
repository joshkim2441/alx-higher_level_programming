#include <stdio.h>
#include <string.h>
#include <Python.h>

/**
 * print_python_string - Prints python strings
 * @p: A PyObject string object
*/
void print_python_string(PyObject *p)
{
	PyObject *s, *r;

	(void)r;

	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	r = PyObject_Repr(p);
	s = PyUnicode_AsEncodedString(p, "utf-8", "~E~");

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	printf("  length: %ld\n", PyUnicode_GET_SIZE(p));
	printf("  value: %s\n", PyBytes_AsString(s));
}
