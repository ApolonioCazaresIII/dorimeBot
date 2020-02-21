# Python Bot specialized for DND

### Help
Commands:
1. `.spec input` 

    This is the command to perform a special check. `input` format:
    
    `(1d10 roll result) (Actual special amount) (special penalty)`
    
    Example, rolling for luck with skill amount 5, 1d10 = 6, penalty = 1
    
    `.spec 6 5 1`


1. `.hit input`

    This is the command to perform a hit check. `input` format:

    `(Ememy AC) (Player ammo AC pen) (player skill) (1d100 roll) (Targeted Attack/Burst Attack penalties) (Player stance mod) (Enemy stance mod)       (Weapon condition pen) (Environment mod) (Vehicle mod) (Enemy cover pen) (Other hit Chance bonuses)`
    
    For example, attacking a mole rat (AC = 7). Using .357 (Ammo AC pen = 7). Player skill in small guns is 100. 1d100 resulted in 25. Using single attack, Standing and enemy is standing. Weapon is in perfect condition. Weather is clear and sunny (day time). Player is not in a vehicle. Enemy is out in the open. No other hit chance bonuses (player is low level and thus has no perks)
    
    `.hit 7 7 100 25 0 0 0 0 0 0 0 0`
    
    
1. `.skill input` 

    This is the command to perform a skill check. This is very similar to .spec `input` format:
    
    `(1d100 roll result) (Actual skill amount) (skill penalty)`
    
    Example, rolling for Small guns with 1d100 = 14, skill amount 100, penalty = 10
    
    `.skill 14 100 10`
    
    
1. `.dmg input`

    This is not fully implemented yet
 
### Terminology
`AC` = Armor Class

`pen` = penalty

`mod` = modifier

### Running bot
Navigate to the bot folder

Type command `python bot.py`

