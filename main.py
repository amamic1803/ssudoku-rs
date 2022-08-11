import os
import sys
from tkinter import *
import math
import time


def resource_path(relative_path):
	""" Get absolute path to resource, works for dev and for PyInstaller """
	try:
		# PyInstaller creates a temp folder and stores path in _MEIPASS
		base_path = sys._MEIPASS
	except Exception:
		base_path = os.path.abspath(".")
	return os.path.join(base_path, relative_path)

def provjera_red(polje, x, y):
	red = polje[x]
	pozicija = polje[x][y]

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
	pozicija = polje[x][y]

	promjena = False

	brojevi_u_stupcu = []
	moguci_brojevi_stupac = []
	for i in range(len(stupac)):
		try:
			len(stupac[i])
			if i != y:
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
	for i in range((math.ceil((x + 1) / 3) - 1) * 3, math.ceil((x + 1) / 3) * 3):
		for j in range((math.ceil((y + 1) / 3) - 1) * 3, math.ceil((y + 1) / 3) * 3):
			kvadrat.append(polje[i][j])
	pozicija = polje[x][y]

	promjena = False

	brojevi_u_kvadratu = []
	moguci_brojevi_kvadrat = []
	for i in range(len(kvadrat)):
		try:
			len(kvadrat[i])
			if i != y:
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

def solve_click():
	fields_dict = {1: a1_txt,
	               2: b1_txt,
	               3: c1_txt,
	               4: d1_txt,
	               5: e1_txt,
	               6: f1_txt,
	               7: g1_txt,
	               8: h1_txt,
	               9: i1_txt,

	               10: a2_txt,
	               11: b2_txt,
	               12: c2_txt,
	               13: d2_txt,
	               14: e2_txt,
	               15: f2_txt,
	               16: g2_txt,
	               17: h2_txt,
	               18: i2_txt,

	               19: a3_txt,
	               20: b3_txt,
	               21: c3_txt,
	               22: d3_txt,
	               23: e3_txt,
	               24: f3_txt,
	               25: g3_txt,
	               26: h3_txt,
	               27: i3_txt,

	               28: a4_txt,
	               29: b4_txt,
	               30: c4_txt,
	               31: d4_txt,
	               32: e4_txt,
	               33: f4_txt,
	               34: g4_txt,
	               35: h4_txt,
	               36: i4_txt,

	               37: a5_txt,
	               38: b5_txt,
	               39: c5_txt,
	               40: d5_txt,
	               41: e5_txt,
	               42: f5_txt,
	               43: g5_txt,
	               44: h5_txt,
	               45: i5_txt,

	               46: a6_txt,
	               47: b6_txt,
	               48: c6_txt,
	               49: d6_txt,
	               50: e6_txt,
	               51: f6_txt,
	               52: g6_txt,
	               53: h6_txt,
	               54: i6_txt,

	               55: a7_txt,
	               56: b7_txt,
	               57: c7_txt,
	               58: d7_txt,
	               59: e7_txt,
	               60: f7_txt,
	               61: g7_txt,
	               62: h7_txt,
	               63: i7_txt,

	               64: a8_txt,
	               65: b8_txt,
	               66: c8_txt,
	               67: d8_txt,
	               68: e8_txt,
	               69: f8_txt,
	               70: g8_txt,
	               71: h8_txt,
	               72: i8_txt,

	               73: a9_txt,
	               74: b9_txt,
	               75: c9_txt,
	               76: d9_txt,
	               77: e9_txt,
	               78: f9_txt,
	               79: g9_txt,
	               80: h9_txt,
	               81: i9_txt}

	"""
	lista = []
	for i in range(1, 74, 9):
		red = []
		for j in range(9):
			x = fields_dict[i + j].get()
			try:
				x = int(x)
				if 1 <= x <= 9:
					red.append(x)
				else:
					red.append([1, 2, 3, 4, 5, 6, 7, 8, 9])
			except ValueError:
				red.append([1, 2, 3, 4, 5, 6, 7, 8, 9])
		lista.append(red)
	del red
	"""

	lista = [[8, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 9, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 2], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 9, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 4, [1, 2, 3, 4, 5, 6, 7, 8, 9]], [7, [1, 2, 3, 4, 5, 6, 7, 8, 9], 2, 1, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 9, 6, [1, 2, 3, 4, 5, 6, 7, 8, 9]], [2, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 9, [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], 6, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 7, [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], 7, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 6, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 5], [[1, 2, 3, 4, 5, 6, 7, 8, 9], 2, 7, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 8, 4, [1, 2, 3, 4, 5, 6, 7, 8, 9], 6], [[1, 2, 3, 4, 5, 6, 7, 8, 9], 3, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 5, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]], [5, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 6, 2, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 8]]

	start_time = time.time()

	promjena = True
	while promjena:
		promjena = False

		for i in range(len(lista)):
			for j in range(len(lista[i])):
				try:
					len(lista[i][j])

					red = provjera_red(lista, i, j)
					if red[1]:
						lista = red[0]
						promjena = True

					stupac = provjera_stupac(lista, i, j)
					if stupac[1]:
						lista = stupac[0]
						promjena = True

					kvadrat = provjera_kvadrat(lista, i, j)
					if kvadrat[1]:
						lista = kvadrat[0]
						promjena = True

				except TypeError:
					pass

	print(time.time() - start_time)

	clear_click()
	for i in range(81):
		fields_dict[i + 1].insert(0, str(lista[i // 9][i % 9]))

def clear_click():
	a1_txt.delete(0, END)
	a2_txt.delete(0, END)
	a3_txt.delete(0, END)
	a4_txt.delete(0, END)
	a5_txt.delete(0, END)
	a6_txt.delete(0, END)
	a7_txt.delete(0, END)
	a8_txt.delete(0, END)
	a9_txt.delete(0, END)
	b1_txt.delete(0, END)
	b2_txt.delete(0, END)
	b3_txt.delete(0, END)
	b4_txt.delete(0, END)
	b5_txt.delete(0, END)
	b6_txt.delete(0, END)
	b7_txt.delete(0, END)
	b8_txt.delete(0, END)
	b9_txt.delete(0, END)
	c1_txt.delete(0, END)
	c2_txt.delete(0, END)
	c3_txt.delete(0, END)
	c4_txt.delete(0, END)
	c5_txt.delete(0, END)
	c6_txt.delete(0, END)
	c7_txt.delete(0, END)
	c8_txt.delete(0, END)
	c9_txt.delete(0, END)
	d1_txt.delete(0, END)
	d2_txt.delete(0, END)
	d3_txt.delete(0, END)
	d4_txt.delete(0, END)
	d5_txt.delete(0, END)
	d6_txt.delete(0, END)
	d7_txt.delete(0, END)
	d8_txt.delete(0, END)
	d9_txt.delete(0, END)
	e1_txt.delete(0, END)
	e2_txt.delete(0, END)
	e3_txt.delete(0, END)
	e4_txt.delete(0, END)
	e5_txt.delete(0, END)
	e6_txt.delete(0, END)
	e7_txt.delete(0, END)
	e8_txt.delete(0, END)
	e9_txt.delete(0, END)
	f1_txt.delete(0, END)
	f2_txt.delete(0, END)
	f3_txt.delete(0, END)
	f4_txt.delete(0, END)
	f5_txt.delete(0, END)
	f6_txt.delete(0, END)
	f7_txt.delete(0, END)
	f8_txt.delete(0, END)
	f9_txt.delete(0, END)
	g1_txt.delete(0, END)
	g2_txt.delete(0, END)
	g3_txt.delete(0, END)
	g4_txt.delete(0, END)
	g5_txt.delete(0, END)
	g6_txt.delete(0, END)
	g7_txt.delete(0, END)
	g8_txt.delete(0, END)
	g9_txt.delete(0, END)
	h1_txt.delete(0, END)
	h2_txt.delete(0, END)
	h3_txt.delete(0, END)
	h4_txt.delete(0, END)
	h5_txt.delete(0, END)
	h6_txt.delete(0, END)
	h7_txt.delete(0, END)
	h8_txt.delete(0, END)
	h9_txt.delete(0, END)
	i1_txt.delete(0, END)
	i2_txt.delete(0, END)
	i3_txt.delete(0, END)
	i4_txt.delete(0, END)
	i5_txt.delete(0, END)
	i6_txt.delete(0, END)
	i7_txt.delete(0, END)
	i8_txt.delete(0, END)
	i9_txt.delete(0, END)


if __name__ == '__main__':
	root = Tk()
	root.title("S-Sudoku")
	root.resizable(False, False)
	root.geometry("281x450")
	root.iconbitmap(resource_path("sudoku-icon.ico"))

	name_lbl = Label(root, text="S-Sudoku", font=("Times New Roman Bold", 25))
	name_lbl.place(width=250, height=50, x=50.5, y=0)

	clr_bt = Button(root, text="Clear", font=("Segoe UI", 9), command=clear_click)
	clr_bt.place(width=50, height=25, x=25, y=325)

	slv_bt = Button(root, text="Solve", font=("Segoe UI", 9), command=solve_click)
	slv_bt.place(width=50, height=25, x=206, y=325)

	a1_txt = Entry(root, font=("Segoe UI", 9))
	a1_txt.place(height=21, width=21, x=25, y=75)
	a2_txt = Entry(root, font=("Segoe UI", 9))
	a2_txt.place(height=21, width=21, x=25, y=99)
	a3_txt = Entry(root, font=("Segoe UI", 9))
	a3_txt.place(height=21, width=21, x=25, y=123)
	a4_txt = Entry(root, font=("Segoe UI", 9))
	a4_txt.place(height=21, width=21, x=25, y=156)
	a5_txt = Entry(root, font=("Segoe UI", 9))
	a5_txt.place(height=21, width=21, x=25, y=180)
	a6_txt = Entry(root, font=("Segoe UI", 9))
	a6_txt.place(height=21, width=21, x=25, y=204)
	a7_txt = Entry(root, font=("Segoe UI", 9))
	a7_txt.place(height=21, width=21, x=25, y=237)
	a8_txt = Entry(root, font=("Segoe UI", 9))
	a8_txt.place(height=21, width=21, x=25, y=261)
	a9_txt = Entry(root, font=("Segoe UI", 9))
	a9_txt.place(height=21, width=21, x=25, y=285)
	b1_txt = Entry(root, font=("Segoe UI", 9))
	b1_txt.place(height=21, width=21, x=49, y=75)
	b2_txt = Entry(root, font=("Segoe UI", 9))
	b2_txt.place(height=21, width=21, x=49, y=99)
	b3_txt = Entry(root, font=("Segoe UI", 9))
	b3_txt.place(height=21, width=21, x=49, y=123)
	b4_txt = Entry(root, font=("Segoe UI", 9))
	b4_txt.place(height=21, width=21, x=49, y=156)
	b5_txt = Entry(root, font=("Segoe UI", 9))
	b5_txt.place(height=21, width=21, x=49, y=180)
	b6_txt = Entry(root, font=("Segoe UI", 9))
	b6_txt.place(height=21, width=21, x=49, y=204)
	b7_txt = Entry(root, font=("Segoe UI", 9))
	b7_txt.place(height=21, width=21, x=49, y=237)
	b8_txt = Entry(root, font=("Segoe UI", 9))
	b8_txt.place(height=21, width=21, x=49, y=261)
	b9_txt = Entry(root, font=("Segoe UI", 9))
	b9_txt.place(height=21, width=21, x=49, y=285)
	c1_txt = Entry(root, font=("Segoe UI", 9))
	c1_txt.place(height=21, width=21, x=73, y=75)
	c2_txt = Entry(root, font=("Segoe UI", 9))
	c2_txt.place(height=21, width=21, x=73, y=99)
	c3_txt = Entry(root, font=("Segoe UI", 9))
	c3_txt.place(height=21, width=21, x=73, y=123)
	c4_txt = Entry(root, font=("Segoe UI", 9))
	c4_txt.place(height=21, width=21, x=73, y=156)
	c5_txt = Entry(root, font=("Segoe UI", 9))
	c5_txt.place(height=21, width=21, x=73, y=180)
	c6_txt = Entry(root, font=("Segoe UI", 9))
	c6_txt.place(height=21, width=21, x=73, y=204)
	c7_txt = Entry(root, font=("Segoe UI", 9))
	c7_txt.place(height=21, width=21, x=73, y=237)
	c8_txt = Entry(root, font=("Segoe UI", 9))
	c8_txt.place(height=21, width=21, x=73, y=261)
	c9_txt = Entry(root, font=("Segoe UI", 9))
	c9_txt.place(height=21, width=21, x=73, y=285)
	d1_txt = Entry(root, font=("Segoe UI", 9))
	d1_txt.place(height=21, width=21, x=106, y=75)
	d2_txt = Entry(root, font=("Segoe UI", 9))
	d2_txt.place(height=21, width=21, x=106, y=99)
	d3_txt = Entry(root, font=("Segoe UI", 9))
	d3_txt.place(height=21, width=21, x=106, y=123)
	d4_txt = Entry(root, font=("Segoe UI", 9))
	d4_txt.place(height=21, width=21, x=106, y=156)
	d5_txt = Entry(root, font=("Segoe UI", 9))
	d5_txt.place(height=21, width=21, x=106, y=180)
	d6_txt = Entry(root, font=("Segoe UI", 9))
	d6_txt.place(height=21, width=21, x=106, y=204)
	d7_txt = Entry(root, font=("Segoe UI", 9))
	d7_txt.place(height=21, width=21, x=106, y=237)
	d8_txt = Entry(root, font=("Segoe UI", 9))
	d8_txt.place(height=21, width=21, x=106, y=261)
	d9_txt = Entry(root, font=("Segoe UI", 9))
	d9_txt.place(height=21, width=21, x=106, y=285)
	e1_txt = Entry(root, font=("Segoe UI", 9))
	e1_txt.place(height=21, width=21, x=130, y=75)
	e2_txt = Entry(root, font=("Segoe UI", 9))
	e2_txt.place(height=21, width=21, x=130, y=99)
	e3_txt = Entry(root, font=("Segoe UI", 9))
	e3_txt.place(height=21, width=21, x=130, y=123)
	e4_txt = Entry(root, font=("Segoe UI", 9))
	e4_txt.place(height=21, width=21, x=130, y=156)
	e5_txt = Entry(root, font=("Segoe UI", 9))
	e5_txt.place(height=21, width=21, x=130, y=180)
	e6_txt = Entry(root, font=("Segoe UI", 9))
	e6_txt.place(height=21, width=21, x=130, y=204)
	e7_txt = Entry(root, font=("Segoe UI", 9))
	e7_txt.place(height=21, width=21, x=130, y=237)
	e8_txt = Entry(root, font=("Segoe UI", 9))
	e8_txt.place(height=21, width=21, x=130, y=261)
	e9_txt = Entry(root, font=("Segoe UI", 9))
	e9_txt.place(height=21, width=21, x=130, y=285)
	f1_txt = Entry(root, font=("Segoe UI", 9))
	f1_txt.place(height=21, width=21, x=154, y=75)
	f2_txt = Entry(root, font=("Segoe UI", 9))
	f2_txt.place(height=21, width=21, x=154, y=99)
	f3_txt = Entry(root, font=("Segoe UI", 9))
	f3_txt.place(height=21, width=21, x=154, y=123)
	f4_txt = Entry(root, font=("Segoe UI", 9))
	f4_txt.place(height=21, width=21, x=154, y=156)
	f5_txt = Entry(root, font=("Segoe UI", 9))
	f5_txt.place(height=21, width=21, x=154, y=180)
	f6_txt = Entry(root, font=("Segoe UI", 9))
	f6_txt.place(height=21, width=21, x=154, y=204)
	f7_txt = Entry(root, font=("Segoe UI", 9))
	f7_txt.place(height=21, width=21, x=154, y=237)
	f8_txt = Entry(root, font=("Segoe UI", 9))
	f8_txt.place(height=21, width=21, x=154, y=261)
	f9_txt = Entry(root, font=("Segoe UI", 9))
	f9_txt.place(height=21, width=21, x=154, y=285)
	g1_txt = Entry(root, font=("Segoe UI", 9))
	g1_txt.place(height=21, width=21, x=187, y=75)
	g2_txt = Entry(root, font=("Segoe UI", 9))
	g2_txt.place(height=21, width=21, x=187, y=99)
	g3_txt = Entry(root, font=("Segoe UI", 9))
	g3_txt.place(height=21, width=21, x=187, y=123)
	g4_txt = Entry(root, font=("Segoe UI", 9))
	g4_txt.place(height=21, width=21, x=187, y=156)
	g5_txt = Entry(root, font=("Segoe UI", 9))
	g5_txt.place(height=21, width=21, x=187, y=180)
	g6_txt = Entry(root, font=("Segoe UI", 9))
	g6_txt.place(height=21, width=21, x=187, y=204)
	g7_txt = Entry(root, font=("Segoe UI", 9))
	g7_txt.place(height=21, width=21, x=187, y=237)
	g8_txt = Entry(root, font=("Segoe UI", 9))
	g8_txt.place(height=21, width=21, x=187, y=261)
	g9_txt = Entry(root, font=("Segoe UI", 9))
	g9_txt.place(height=21, width=21, x=187, y=285)
	h1_txt = Entry(root, font=("Segoe UI", 9))
	h1_txt.place(height=21, width=21, x=211, y=75)
	h2_txt = Entry(root, font=("Segoe UI", 9))
	h2_txt.place(height=21, width=21, x=211, y=99)
	h3_txt = Entry(root, font=("Segoe UI", 9))
	h3_txt.place(height=21, width=21, x=211, y=123)
	h4_txt = Entry(root, font=("Segoe UI", 9))
	h4_txt.place(height=21, width=21, x=211, y=156)
	h5_txt = Entry(root, font=("Segoe UI", 9))
	h5_txt.place(height=21, width=21, x=211, y=180)
	h6_txt = Entry(root, font=("Segoe UI", 9))
	h6_txt.place(height=21, width=21, x=211, y=204)
	h7_txt = Entry(root, font=("Segoe UI", 9))
	h7_txt.place(height=21, width=21, x=211, y=237)
	h8_txt = Entry(root, font=("Segoe UI", 9))
	h8_txt.place(height=21, width=21, x=211, y=261)
	h9_txt = Entry(root, font=("Segoe UI", 9))
	h9_txt.place(height=21, width=21, x=211, y=285)
	i1_txt = Entry(root, font=("Segoe UI", 9))
	i1_txt.place(height=21, width=21, x=235, y=75)
	i2_txt = Entry(root, font=("Segoe UI", 9))
	i2_txt.place(height=21, width=21, x=235, y=99)
	i3_txt = Entry(root, font=("Segoe UI", 9))
	i3_txt.place(height=21, width=21, x=235, y=123)
	i4_txt = Entry(root, font=("Segoe UI", 9))
	i4_txt.place(height=21, width=21, x=235, y=156)
	i5_txt = Entry(root, font=("Segoe UI", 9))
	i5_txt.place(height=21, width=21, x=235, y=180)
	i6_txt = Entry(root, font=("Segoe UI", 9))
	i6_txt.place(height=21, width=21, x=235, y=204)
	i7_txt = Entry(root, font=("Segoe UI", 9))
	i7_txt.place(height=21, width=21, x=235, y=237)
	i8_txt = Entry(root, font=("Segoe UI", 9))
	i8_txt.place(height=21, width=21, x=235, y=261)
	i9_txt = Entry(root, font=("Segoe UI", 9))
	i9_txt.place(height=21, width=21, x=235, y=285)

	root.mainloop()
	sys.exit()
