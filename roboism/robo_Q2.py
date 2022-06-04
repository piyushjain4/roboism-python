def hidden_crdt_no(card_no):
    asterisk = "************"
    sliced_no = card_no[12:16]
    credit_no = asterisk +sliced_no
    return credit_no

num =hidden_crdt_no("3864778676325672")
print(num) 