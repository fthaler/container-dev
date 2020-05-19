def Settings(**kwargs):
    return {
        'flags': [
            '-x', 'c++', '-Wall', '-Wextra', '-std=c++14',
            '-DGTBENCH_FLOAT=double', '-DGTBENCH_BACKEND=cpu_ifirst',
            '-I/usr/include/x86_64-linux-gnu/openmpi'
        ]
    }
