from nada_dsl import *

def nada_main():
    party1 = Party(name='Party1')
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # Compute the sum, product, and difference of the input integers
    sum_result = my_int1 + my_int2
    product_result = my_int1 * my_int2
    difference_result = my_int1 - my_int2

    # Compute the maximum and minimum of the two integers
    max_result = If(my_int1 > my_int2, my_int1, my_int2)
    min_result = If(my_int1 < my_int2, my_int1, my_int2)

    # Return all results as outputs
    return [
        Output(sum_result, "sum_output", party1),
        Output(product_result, "product_output", party1),
        Output(difference_result, "difference_output", party1),
        Output(max_result, "max_output", party1),
        Output(min_result, "min_output", party1)
    ]
