import rust


def is_entry_valid(polje):
	valid = True
	for x in range(9):
		for y in range(9):
			if type(polje[x][y]) == int:
				pozicija = polje[x][y]
				red = [z for z in polje[x] if type(z) == int]
				stupac = []
				for i in range(9):
					if type(polje[i][y]) == int:
						stupac.append(polje[i][y])
				kvadrat = []
				for i in range(((x // 3) * 3), (((x // 3) + 1) * 3)):
					for j in range(((y // 3) * 3), (((y // 3) + 1) * 3)):
						if type(polje[i][j]) == int:
							kvadrat.append(polje[i][j])
				if red.count(pozicija) > 1 or stupac.count(pozicija) > 1 or kvadrat.count(pozicija) > 1:
					valid = False
					break
		if not valid:
			break
	return valid

def is_solution_valid(polje):
	num_field_int = 0
	valid = True
	for x in range(9):
		for y in range(9):
			if type(polje) == int:
				num_field_int += 1
				pozicija = polje[x][y]
				red = [z for z in polje[x] if type(z) == int]
				stupac = []
				for i in range(9):
					if type(polje[i][y]) == int:
						stupac.append(polje[i][y])
				kvadrat = []
				for i in range(((x // 3) * 3), (((x // 3) + 1) * 3)):
					for j in range(((y // 3) * 3), (((y // 3) + 1) * 3)):
						if type(polje[i][j]) == int:
							kvadrat.append(polje[i][j])
				if red.count(pozicija) > 1 or stupac.count(pozicija) > 1 or kvadrat.count(pozicija) > 1:
					valid = False
					break
		if not valid:
			break
	if valid and num_field_int == 81:
		return True
	else:
		return False

def provjera_red(polje, x, y):
	red = polje[x]
	pozicija = polje[x][y].copy()

	promjena = False

	brojevi_u_redu = []
	moguci_brojevi_red = []
	for i in range(len(red)):
		try:
			len(red[i])
			if i != y:
				moguci_brojevi_red.extend(red[i])
		except TypeError:
			brojevi_u_redu.append(red[i])

	izbrisano = 0
	for i in range(len(pozicija)):
		if pozicija[i - izbrisano] in brojevi_u_redu:
			del pozicija[i - izbrisano]
			izbrisano += 1
			promjena = True

	for i in pozicija:
		if i not in moguci_brojevi_red:
			pozicija = [i]
			promjena = True
			break

	del polje[x][y]
	if len(pozicija) == 1:
		polje[x].insert(y, pozicija[0])
	else:
		polje[x].insert(y, pozicija)

	return polje, promjena

def provjera_stupac(polje, x, y):
	stupac = []
	for i in range(9):
		stupac.append(polje[i][y])
	pozicija = polje[x][y].copy()
	promjena = False

	brojevi_u_stupcu = []
	moguci_brojevi_stupac = []
	for i in range(len(stupac)):
		try:
			len(stupac[i])
			if i != x:
				moguci_brojevi_stupac.extend(stupac[i])
		except TypeError:
			brojevi_u_stupcu.append(stupac[i])
	izbrisano = 0
	for i in range(len(pozicija)):
		if pozicija[i - izbrisano] in brojevi_u_stupcu:
			del pozicija[i - izbrisano]
			izbrisano += 1
			promjena = True
	for i in pozicija:
		if i not in moguci_brojevi_stupac:
			pozicija = [i]
			promjena = True
			break
	del polje[x][y]
	if len(pozicija) == 1:
		polje[x].insert(y, pozicija[0])
	else:
		polje[x].insert(y, pozicija)

	return polje, promjena

def provjera_kvadrat(polje, x, y):
	kvadrat = []
	for i in range(((x // 3) * 3), (((x // 3) + 1) * 3)):
		for j in range(((y // 3) * 3), (((y // 3) + 1) * 3)):
			kvadrat.append(polje[i][j])
	pozicija = polje[x][y].copy()

	promjena = False

	brojevi_u_kvadratu = []
	moguci_brojevi_kvadrat = []
	for i in range(len(kvadrat)):
		try:
			len(kvadrat[i])
			if (((x // 3) * 3) + (i // 3)) != x or (((y // 3) * 3) + (i % 3)) != y:
				moguci_brojevi_kvadrat.extend(kvadrat[i])
		except TypeError:
			brojevi_u_kvadratu.append(kvadrat[i])

	izbrisano = 0
	for i in range(len(pozicija)):
		if pozicija[i - izbrisano] in brojevi_u_kvadratu:
			del pozicija[i - izbrisano]
			izbrisano += 1
			promjena = True

	for i in pozicija:
		if i not in moguci_brojevi_kvadrat:
			pozicija = [i]
			promjena = True
			break

	del polje[x][y]
	if len(pozicija) == 1:
		polje[x].insert(y, pozicija[0])
	else:
		polje[x].insert(y, pozicija)
	return polje, promjena

def provjera_parovi_redovi(polje):
	promjena = False
	for z in range(9):
		red = polje[z]
		red_dict = {}
		for i in range(len(red)):
			if type(red[i]) == list:
				for j in red[i]:
					if j in red_dict.keys():
						red_dict[j][0] += 1
						red_dict[j][1].append(i)
					else:
						red_dict[j] = [1, [i]]
		possible_pair_digits = []
		for i in red_dict.keys():
			if red_dict[i][0] == 2:
				possible_pair_digits.append(i)
		pozicije_parova = []
		parovi = []
		for i in possible_pair_digits:
			for j in possible_pair_digits:
				if i != j:
					broj_istih_pozicija = 0
					iste_pozicije = []
					for x in red_dict[i][1]:
						if x in red_dict[j][1]:
							broj_istih_pozicija += 1
							iste_pozicije.append(x)
					if broj_istih_pozicija == 2:
						pair = [i, j]
						pair.sort()
						if pair not in parovi:
							pozicije_parova.append(iste_pozicije)
							parovi.append(pair)

		for i in range(len(parovi)):
			if polje[z][pozicije_parova[i][0]] != parovi[i]:
				promjena = True
				polje[z][pozicije_parova[i][0]] = parovi[i].copy()
			if polje[z][pozicije_parova[i][1]] != parovi[i]:
				promjena = True
				polje[z][pozicije_parova[i][1]] = parovi[i].copy()

	return polje, promjena

def provjera_parovi_stupci(polje):
	promjena = False
	for z in range(9):
		stupac = []
		for i in range(9):
			stupac.append(polje[i][z])
		stupac_dict = {}
		for i in range(len(stupac)):
			if type(stupac[i]) == list:
				for j in stupac[i]:
					if j in stupac_dict.keys():
						stupac_dict[j][0] += 1
						stupac_dict[j][1].append(i)
					else:
						stupac_dict[j] = [1, [i]]
		possible_pair_digits = []
		for i in stupac_dict.keys():
			if stupac_dict[i][0] == 2:
				possible_pair_digits.append(i)
		pozicije_parova = []
		parovi = []
		for i in possible_pair_digits:
			for j in possible_pair_digits:
				if i != j:
					broj_istih_pozicija = 0
					iste_pozicije = []
					for x in stupac_dict[i][1]:
						if x in stupac_dict[j][1]:
							broj_istih_pozicija += 1
							iste_pozicije.append(x)
					if broj_istih_pozicija == 2:
						pair = [i, j]
						pair.sort()
						if pair not in parovi:
							pozicije_parova.append(iste_pozicije)
							parovi.append(pair)

		for i in range(len(parovi)):
			if polje[pozicije_parova[i][0]][z] != parovi[i]:
				promjena = True
				polje[pozicije_parova[i][0]][z] = parovi[i].copy()
			if polje[pozicije_parova[i][1]][z] != parovi[i]:
				promjena = True
				polje[pozicije_parova[i][1]][z] = parovi[i].copy()

	return polje, promjena

def provjera_parovi_kvadrati(polje):
	promjena = False
	for x_start in range(0, 7, 3):
		for y_start in range(0, 7, 3):
			kvadrat = []
			for i in range(((x_start // 3) * 3), (((x_start // 3) + 1) * 3)):
				for j in range(((y_start // 3) * 3), (((y_start // 3) + 1) * 3)):
					kvadrat.append(polje[i][j])
			kvadrat_dict = {}
			for i in range(len(kvadrat)):
				if type(kvadrat[i]) == list:
					for j in kvadrat[i]:
						if j in kvadrat_dict.keys():
							kvadrat_dict[j][0] += 1
							kvadrat_dict[j][1].append(i)
						else:
							kvadrat_dict[j] = [1, [i]]
			possible_pair_digits = []
			for i in kvadrat_dict.keys():
				if kvadrat_dict[i][0] == 2:
					possible_pair_digits.append(i)
			pozicije_parova = []
			parovi = []
			for i in possible_pair_digits:
				for j in possible_pair_digits:
					if i != j:
						broj_istih_pozicija = 0
						iste_pozicije = []
						for x in kvadrat_dict[i][1]:
							if x in kvadrat_dict[j][1]:
								broj_istih_pozicija += 1
								iste_pozicije.append(x)
						if broj_istih_pozicija == 2:
							pair = [i, j]
							pair.sort()
							if pair not in parovi:
								pozicije_parova.append(iste_pozicije)
								parovi.append(pair)

			for i in range(len(parovi)):
				if polje[x_start + (pozicije_parova[i][0] // 3)][y_start + (pozicije_parova[i][0] % 3)] != parovi[i]:
					promjena = True
					polje[x_start + (pozicije_parova[i][0] // 3)][y_start + (pozicije_parova[i][0] % 3)] = parovi[i].copy()
				if polje[x_start + (pozicije_parova[i][1] // 3)][y_start + (pozicije_parova[i][1] % 3)] != parovi[i]:
					promjena = True
					polje[x_start + (pozicije_parova[i][1] // 3)][y_start + (pozicije_parova[i][1] % 3)] = parovi[i].copy()

	return polje, promjena

def provjera_xwing_redovi(polje):
	promjena = False

	svi_redovi = []
	for z in range(9):
		red = polje[z]
		red_dict = {}

		for i in range(len(red)):
			if type(red[i]) == list:
				for j in red[i]:
					if j in red_dict.keys():
						red_dict[j][0] += 1
						red_dict[j][1].append(i)
					else:
						red_dict[j] = [1, [i]]

		ispis = {}
		for i in red_dict.keys():
			if red_dict[i][0] == 2:
				ispis[i] = red_dict[i][1]

		svi_redovi.append(ispis)

	xwing = []  # [[broj, [red1, red2], [pozicija1, pozicija2]]]
	for z in range(9):
		for x in svi_redovi[z].keys():
			for y in range(z + 1, 9):
				if x in svi_redovi[y].keys():
					if svi_redovi[y][x] == svi_redovi[z][x]:
						xwing.append([x, [z, y], svi_redovi[z][x]].copy())

	for x in range(len(xwing)):
		for y in range(9):
			if y != xwing[x][1][0] and y != xwing[x][1][1]:
				try:
					polje[y][xwing[x][2][0]].remove(xwing[x][0])
					promjena = True
				except (TypeError, ValueError, AttributeError):
					pass
				try:
					polje[y][xwing[x][2][1]].remove(xwing[x][0])
					promjena = True
				except (TypeError, ValueError, AttributeError):
					pass

	return polje, promjena

def provjera_xwing_stupci(polje):
	promjena = False

	svi_stupci = []
	for z in range(9):
		stupac = []
		for i in range(9):
			stupac.append(polje[i][z])

		stupac_dict = {}

		for i in range(len(stupac)):
			if type(stupac[i]) == list:
				for j in stupac[i]:
					if j in stupac_dict.keys():
						stupac_dict[j][0] += 1
						stupac_dict[j][1].append(i)
					else:
						stupac_dict[j] = [1, [i]]

		ispis = {}
		for i in stupac_dict.keys():
			if stupac_dict[i][0] == 2:
				ispis[i] = stupac_dict[i][1]

		svi_stupci.append(ispis)

	xwing = []  # [[broj, [stupac1, stupac2], [pozicija1, pozicija2]]]
	for z in range(9):
		for x in svi_stupci[z].keys():
			for y in range(z + 1, 9):
				if x in svi_stupci[y].keys():
					if svi_stupci[y][x] == svi_stupci[z][x]:
						xwing.append([x, [z, y], svi_stupci[z][x]].copy())

	for x in range(len(xwing)):
		for y in range(9):
			if y != xwing[x][1][0] and y != xwing[x][1][1]:
				try:
					polje[xwing[x][2][0]][y].remove(xwing[x][0])
					promjena = True
				except (TypeError, ValueError, AttributeError):
					pass
				try:
					polje[xwing[x][2][1]][y].remove(xwing[x][0])
					promjena = True
				except (TypeError, ValueError, AttributeError):
					pass

	return polje, promjena

def solve_with_rust(polje):
	rust_input_string = ""
	for i in range(9):
		for j in range(9):
			if type(polje[i][j]) == int:
				rust_input_string += f"{polje[i][j]}"
			else:
				rust_input_string += "."
	rust_output_string = rust.solve_sudoku(rust_input_string)
	if rust_output_string == "0":
		return False, polje
	else:
		for i in range(81):
			polje[i // 9][i % 9] = int(rust_output_string[i])
		return True, polje

def solve_sudoku(field):
	# field = lista_easy = [[8, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 9, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 2], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 9, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 4, [1, 2, 3, 4, 5, 6, 7, 8, 9]], [7, [1, 2, 3, 4, 5, 6, 7, 8, 9], 2, 1, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 9, 6, [1, 2, 3, 4, 5, 6, 7, 8, 9]], [2, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 9, [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], 6, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 7, [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], 7, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 6, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 5], [[1, 2, 3, 4, 5, 6, 7, 8, 9], 2, 7, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 8, 4, [1, 2, 3, 4, 5, 6, 7, 8, 9], 6], [[1, 2, 3, 4, 5, 6, 7, 8, 9], 3, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 5, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]], [5, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 6, 2, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 8]]
	# field = lista_medium = [[[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 8, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 5, [1, 2, 3, 4, 5, 6, 7, 8, 9], 9], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 6, 9, [1, 2, 3, 4, 5, 6, 7, 8, 9], 1, 2, [1, 2, 3, 4, 5, 6, 7, 8, 9]], [9, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 3], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 7, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 4, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]], [4, [1, 2, 3, 4, 5, 6, 7, 8, 9], 6, [1, 2, 3, 4, 5, 6, 7, 8, 9], 3, [1, 2, 3, 4, 5, 6, 7, 8, 9], 2, [1, 2, 3, 4, 5, 6, 7, 8, 9], 7], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 2, 1, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 9, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]], [6, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 2], [[1, 2, 3, 4, 5, 6, 7, 8, 9], 2, 8, [1, 2, 3, 4, 5, 6, 7, 8, 9], 6, 7, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]], [1, [1, 2, 3, 4, 5, 6, 7, 8, 9], 3, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 2, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]]]
	# field = lista_hard = [[[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 6, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 7, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 8, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 2], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 1, 7, [1, 2, 3, 4, 5, 6, 7, 8, 9], 9, 4, [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 2, [1, 2, 3, 4, 5, 6, 7, 8, 9], 9, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 1, [1, 2, 3, 4, 5, 6, 7, 8, 9]], [6, [1, 2, 3, 4, 5, 6, 7, 8, 9], 4, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 5, [1, 2, 3, 4, 5, 6, 7, 8, 9], 7], [[1, 2, 3, 4, 5, 6, 7, 8, 9], 1, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 5, [1, 2, 3, 4, 5, 6, 7, 8, 9], 2, 9, [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], 8, 9, [1, 2, 3, 4, 5, 6, 7, 8, 9], 2, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]], [3, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 4, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 7, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 1, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]]]
	# field = lista_very_hard = [[3, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 4], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 3, [1, 2, 3, 4, 5, 6, 7, 8, 9], 7, 5], [[1, 2, 3, 4, 5, 6, 7, 8, 9], 7, 1, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 6, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 5, 4, 9, [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], 3, [1, 2, 3, 4, 5, 6, 7, 8, 9], 2, [1, 2, 3, 4, 5, 6, 7, 8, 9], 6, [1, 2, 3, 4, 5, 6, 7, 8, 9], 5, [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], 9, 2, 7, 4, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 3, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 5, 1, [1, 2, 3, 4, 5, 6, 7, 8, 9]], [6, 8, [1, 2, 3, 4, 5, 6, 7, 8, 9], 9, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]], [2, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 7]]
	# field = lista_impossible = [[[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 2, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 9], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 9, [1, 2, 3, 4, 5, 6, 7, 8, 9], 6, [1, 2, 3, 4, 5, 6, 7, 8, 9], 7, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], 7, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 8, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 1, 6], [5, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 4], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 8, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 5, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]], [4, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 6, 7], [6, 2, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 1, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 4, [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 1, [1, 2, 3, 4, 5, 6, 7, 8, 9], 5, [1, 2, 3, 4, 5, 6, 7, 8, 9], 2, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]], [8, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 3, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]]]
	# return codes: 0 - invalid entry | 1 - valid solution | 2 - invalid solution
	if not is_entry_valid(field):
		return 0, field

	promjena = True
	while promjena:
		promjena = False

		# scanning
		promjena_scanning = True
		while promjena_scanning:
			promjena_scanning = False
			for i in range(len(field)):
				for j in range(len(field[i])):
					if type(field[i][j]) == list:
						red = provjera_red(field, i, j)
						if red[1]:
							field = red[0]
							promjena = True
							promjena_scanning = True
					if type(field[i][j]) == list:
						stupac = provjera_stupac(field, i, j)
						if stupac[1]:
							field = stupac[0]
							promjena = True
							promjena_scanning = True
					if type(field[i][j]) == list:
						kvadrat = provjera_kvadrat(field, i, j)
						if kvadrat[1]:
							field = kvadrat[0]
							promjena = True
							promjena_scanning = True

		# pairs
		parovi_redovi = provjera_parovi_redovi(field)
		if parovi_redovi[1]:
			field = parovi_redovi[0]
			promjena = True

		parovi_stupci = provjera_parovi_stupci(field)
		if parovi_stupci[1]:
			field = parovi_stupci[0]
			promjena = True

		parovi_kvadrati = provjera_parovi_kvadrati(field)
		if parovi_kvadrati[1]:
			field = parovi_kvadrati[0]
			promjena = True

		# x wing
		xwing_redovi = provjera_xwing_redovi(field)
		if xwing_redovi[1]:
			field = xwing_redovi[0]
			promjena = True

		xwing_stupci = provjera_xwing_stupci(field)
		if xwing_stupci[1]:
			field = xwing_stupci[0]
			promjena = True

	if is_solution_valid(field):
		return 1, field
	else:
		rust_solution = solve_with_rust(field)
		if rust_solution[0]:
			field = rust_solution[1]
			return 1, field
		else:
			return 2, field


if __name__ == '__main__':

	# field = lista_easy = [[8, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 9, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 2], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 9, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 4, [1, 2, 3, 4, 5, 6, 7, 8, 9]], [7, [1, 2, 3, 4, 5, 6, 7, 8, 9], 2, 1, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 9, 6, [1, 2, 3, 4, 5, 6, 7, 8, 9]], [2, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 9, [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], 6, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 7, [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], 7, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 6, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 5], [[1, 2, 3, 4, 5, 6, 7, 8, 9], 2, 7, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 8, 4, [1, 2, 3, 4, 5, 6, 7, 8, 9], 6], [[1, 2, 3, 4, 5, 6, 7, 8, 9], 3, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 5, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]], [5, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 6, 2, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 8]]
	# field = lista_medium = [[[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 8, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 5, [1, 2, 3, 4, 5, 6, 7, 8, 9], 9], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 6, 9, [1, 2, 3, 4, 5, 6, 7, 8, 9], 1, 2, [1, 2, 3, 4, 5, 6, 7, 8, 9]], [9, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 3], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 7, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 4, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]], [4, [1, 2, 3, 4, 5, 6, 7, 8, 9], 6, [1, 2, 3, 4, 5, 6, 7, 8, 9], 3, [1, 2, 3, 4, 5, 6, 7, 8, 9], 2, [1, 2, 3, 4, 5, 6, 7, 8, 9], 7], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 2, 1, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 9, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]], [6, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 2], [[1, 2, 3, 4, 5, 6, 7, 8, 9], 2, 8, [1, 2, 3, 4, 5, 6, 7, 8, 9], 6, 7, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]], [1, [1, 2, 3, 4, 5, 6, 7, 8, 9], 3, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 2, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]]]
	# field = lista_hard = [[[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 6, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 7, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 8, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 2], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 1, 7, [1, 2, 3, 4, 5, 6, 7, 8, 9], 9, 4, [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 2, [1, 2, 3, 4, 5, 6, 7, 8, 9], 9, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 1, [1, 2, 3, 4, 5, 6, 7, 8, 9]], [6, [1, 2, 3, 4, 5, 6, 7, 8, 9], 4, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 5, [1, 2, 3, 4, 5, 6, 7, 8, 9], 7], [[1, 2, 3, 4, 5, 6, 7, 8, 9], 1, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 5, [1, 2, 3, 4, 5, 6, 7, 8, 9], 2, 9, [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], 8, 9, [1, 2, 3, 4, 5, 6, 7, 8, 9], 2, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]], [3, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 4, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 7, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 1, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]]]
	# field = lista_very_hard = [[3, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 4], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 3, [1, 2, 3, 4, 5, 6, 7, 8, 9], 7, 5], [[1, 2, 3, 4, 5, 6, 7, 8, 9], 7, 1, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 6, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 5, 4, 9, [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], 3, [1, 2, 3, 4, 5, 6, 7, 8, 9], 2, [1, 2, 3, 4, 5, 6, 7, 8, 9], 6, [1, 2, 3, 4, 5, 6, 7, 8, 9], 5, [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], 9, 2, 7, 4, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 3, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 5, 1, [1, 2, 3, 4, 5, 6, 7, 8, 9]], [6, 8, [1, 2, 3, 4, 5, 6, 7, 8, 9], 9, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]], [2, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 7]]
	field = lista_impossible = [[[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 2, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 9], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 9, [1, 2, 3, 4, 5, 6, 7, 8, 9], 6, [1, 2, 3, 4, 5, 6, 7, 8, 9], 7, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], 7, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 8, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 1, 6], [5, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 4], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 8, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 5, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]], [4, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 6, 7], [6, 2, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 1, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 4, [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 1, [1, 2, 3, 4, 5, 6, 7, 8, 9], 5, [1, 2, 3, 4, 5, 6, 7, 8, 9], 2, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]], [8, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 3, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]]]

	solution = solve_sudoku(field)
	print(f"{solution[0]}\n{solution[1]}")
