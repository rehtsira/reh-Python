imoney = 550
iwater = 400
imilk = 540
ibeans = 120
icup = 9

def init_status():
  print("The coffee machine has:\n" + str(iwater) + " of water\n" + str(imilk) + " of milk\n" + str(ibeans) + " of coffee beans\n" + str(icup) + " of disposable cups\n" + str(imoney) + " of money")

init_status()

def action():
  do = input("Write action (buy, fill, take):\n")
  if do == "buy":
    dobuy = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino\n")
    if dobuy == '1':
      w = iwater - 250
      m = imilk
      b = ibeans - 16
      mon = imoney + 4
      c = icup - 1
      print("The coffee machine has:\n" + str(w) + " of water\n" + str(m) + " of milk\n" + str(b) + " of coffee beans\n" + str(c) + " of disposable cups\n" + str(mon) + " of money")
    if dobuy == '2':
      w = iwater - 350
      m = imilk - 75
      b = ibeans - 20
      mon = imoney + 7
      c = icup - 1
      print("The coffee machine has:\n" + str(w) + " of water\n" + str(m) + " of milk\n" + str(b) + " of coffee beans\n" + str(c) + " of disposable cups\n" + str(mon) + " of money")
    if dobuy == '3':
      w = iwater - 200
      m = imilk - 100
      b = ibeans - 12
      mon = imoney + 6
      c = icup - 1
      print("The coffee machine has:\n" + str(w) + " of water\n" + str(m) + " of milk\n" + str(b) + " of coffee beans\n" + str(c) + " of disposable cups\n" + str(mon) + " of money")
  if do == "fill":
    fillwater = input("Write how many ml of water do you want to add:\n")
    fillmilk = input("Write how many mlm of milk do you want to add:\n")
    fillbean = input("Write how many grams of coffee beans do you want to add:\n")
    fillcup = input("Write how many disposable cups of coffee do you want to add:\n")
    w = int(fillwater) + int(iwater)
    m = int(fillmilk) + int(imilk)
    b = int(fillbean) + int(ibeans)
    c = int(fillcup) + int(icup)
    print("The coffee machine has:\n" + str(w) + " of water\n" + str(m) + " of milk\n" + str(b) + " of coffee beans\n" + str(c) + " of disposable cups\n" + str(imoney) + " of money")
  if do == "take":
    print("I give you " + str(imoney))
    print("The coffee machine has:\n" + str(iwater) + " of water\n" + str(imilk) + " of milk\n" + str(ibeans) + " of coffee beans\n" + str(icup) + " of disposable cups\n" + "0 of money")

action()



