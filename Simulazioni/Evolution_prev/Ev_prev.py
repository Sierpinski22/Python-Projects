def chi(oss, att):
    return ((oss - att) ** 2) / att


def prevision(o_dom, e, o_rec, t1_, t2_, t3_, depth):
    tot_ind = o_dom + e + o_rec
    tot_all = tot_ind * 2
    allele_1 = o_dom * 2 + e
    allele_2 = o_rec * 2 + e
    p = allele_1 / tot_all
    q = allele_2 / tot_all
    print(f"\nGenerazione f{depth}\n")
    print(f"p = {p:.4f}\nq = {q:.4f}\n")
    pre_o_dom = p * p
    pre_e = 2 * p * q
    pre_o_rec = q * q
    print(f"p^2 = {p * p:.4f}\n2pq = {q * p * 2:.4f}\nq^2 = {q * q:.4f}\n")
    chi_squared = chi(o_dom, pre_o_dom * tot_ind) + chi(e, pre_e * tot_ind) + chi(o_rec, pre_o_rec * tot_ind)
    new_o_dom = pre_o_dom * tot_ind * t1_
    new_e = pre_e * tot_ind * t2_
    new_o_rec = pre_o_rec * tot_ind * t3_
    actual_ind = new_o_rec + new_o_dom + new_e
    if chi_squared < 6.64:
        disc = "la popolazione è stabile"
    elif 6.64 < chi_squared < 10.83:
        disc = "c'è incertezza circa stabilità o evoluzione"
    else:
        disc = "la popolazione è in evoluzione"

    print(f"Percentuale omozigoti 'dominanti': {pre_o_dom * 100:.1f}%, quantità prevista: {new_o_dom:.1f}, "
          f"percentuale esatta: {new_o_dom / actual_ind * 100:.1f}%")
    print(f"Percentuale eterozigoti e quantità prevista: {pre_e * 100:.1f}%, quantità presvista: {new_e:.1f}, "
          f"percentuale esatta: {new_e / actual_ind * 100:.1f}%")
    print(f"Percentuale omozigoti 'recessivi': {pre_o_rec * 100:.1f}%, quantità prevista: {new_o_rec:.1f}, "
          f"percentuale esatta: {new_o_rec / actual_ind * 100:.1f}%")
    print(f"Chi quadro = {chi_squared:.3f}: " + disc)
    print('\n' + "=" * 120)
    return new_o_dom, new_e, new_o_rec


while True:
    print("Generazione p:")
    AA = int(input("    Numero di individui omozigoti 'dominanti' > "))
    Aa = int(input("    Numero di individui eterozigoti > "))
    aa = int(input("    Numero di individui omozigoti 'recessivi' > "))
    t1 = float(input("\n    Tasso di sopravvivenza omozigoti 'dominanti' > ")) / 100
    t2 = float(input("    Tasso di sopravvivenza eterozigoti > ")) / 100
    t3 = float(input("    Tasso di sopravvivenza omozigoti 'recessivi' > ")) / 100
    #n = int(input("    Numero di generazioni > "))
    print('')
    i = 0
    #for i in range(0, n):
    prevision(AA, Aa, aa, t1, t2, t3, i + 1)

