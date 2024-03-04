# Behind the Scenes

## Challenge Details 

- **CTF:** Hack The Box
- **Category:** Reversing
- **Points:** 10

## Provided Materials

- `ELF 64-bit LSB pie executable`

## Solution

We can decompile it online [here](https://dogbolt.org):

```sh
int sub_40132f()
{
    struct_0 *v1;  // [bp+0xfff58]

    if (strncmp(v1->field_8, "Itz", 3))
        [D] Unsupported jumpkind Ijk_NoDecode at address 4199465
    [D] Unsupported jumpkind Ijk_NoDecode at address 4199257
}

typedef struct struct_0 {
    char padding_0[8];
    unsigned long long field_8;
} struct_0;

int sub_40135b()
{
    struct_0 *v1;  // [bp+0xfff58]

    if (strncmp(v1->field_8 + 3, "_0n", 3))
        [D] Unsupported jumpkind Ijk_NoDecode at address 4199456
    [D] Unsupported jumpkind Ijk_NoDecode at address 4199305
}

typedef struct struct_0 {
    char padding_0[8];
    unsigned long long field_8;
} struct_0;

int sub_40138b()
{
    struct_0 *v1;  // [bp+0xfff58]

    if (strncmp(v1->field_8 + 6, "Ly_", 3))
        [D] Unsupported jumpkind Ijk_NoDecode at address 4199447
    [D] Unsupported jumpkind Ijk_NoDecode at address 4199349
}

typedef struct struct_0 {
    char padding_0[8];
    unsigned long long field_8;
} struct_0;

int sub_4013b7()
{
    struct_0 *v1;  // [bp+0xfff58]

    if (strncmp(v1->field_8 + 9, "UD2", 3))
        [D] Unsupported jumpkind Ijk_NoDecode at address 4199438
    [D] Unsupported jumpkind Ijk_NoDecode at address 4199393
}
```

We can see 4 `strncmp` functions, so we can directly build the string:

`Itz_0nLy_UD2`

## Final Flag

`HTB{Itz_0nLy_UD2)`

*Created by [bu19akov](https://github.com/bu19akov)*