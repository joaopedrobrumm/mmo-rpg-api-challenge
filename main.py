class Player:
    """A simple example class"""
    health = 100

    def attack(self, damage, otherPlayer):
        otherPlayer.health = otherPlayer.health - damage
        return 'deu dano ' + str(damage)
    

player1 = Player()
player2 = Player()

print("VIDA DO P2 ANTES DO ATAQUE", player2.health)

result = player1.attack(4, player2)

print("VIDA DO P2 DEPOIS DO ATAQUE", player2.health)

print(result)

