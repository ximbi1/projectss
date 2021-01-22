#include <iostream>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>
using namespace std;

int createZombie() {
    if (rand() % 67 < 10)
    {
        return 11;
    }
    else
    {
        return rand() % 10 + 1;
    }    
}

int main() {
    srand(time(NULL));
    char enter;

    // game stats
    int playerAlive = true;
    int PlayerSkill = 9;
    int playerScore = 1;
    string playerName = "";
    int zombieCount = 0;
    int zombieKilled = 0;

    // title
    cout << "Welcome to Zombie war." 
    << endl << "Press [ENTER] to start.";
    cin.get();

    // player name
    cout << "Please enter your name:";
    cin >> playerName;

    // ask how many zombies
    cout << "How many zombies do you wish to fight? ";
    cin >> zombieCount;

    cout << "Get ready to fight for your life, " << playerName << "!" << endl;

    // main game loop
    while (playerAlive && zombieKilled < zombieCount )
    {
        // create a random zombie
        int zombieSkill = createZombie();

        // battle sequence
        if (zombieSkill > 10)
        {
            cout << endl << "Here comes zombie " << zombieKilled + 1 << endl;
        }
        else
        {
            cout << endl << "Here comes zombie " << zombieKilled + 1 << endl;
        }
        cout << "Fighting..." << endl;
        sleep(2);

        // zombie killed the player 
        if (PlayerSkill < zombieSkill)
        {
            playerAlive = false;
            cout << "You have died." << endl;
        }
        // player killed the zombie
        else
        {
            if (PlayerSkill - zombieSkill > 7)
            {
                cout << "You wasted the zombie!" << endl;
                playerScore = playerScore * 2;
            }
            else if (PlayerSkill - zombieSkill > 5)
            {
                cout << "You decapitated the zombie!" << endl;
                playerScore = playerScore * 2;
            }
            else if (PlayerSkill - zombieSkill > 0)
            {
                cout << "You killed the zombie!" << endl;
                playerScore = playerScore * 2;
            }
            else
            {
                cout << "You killed the zombie, but suffered injures." << endl;
            }
            zombieKilled++;
        }
        
        cout << endl;
        sleep(1);
        
    }

    // end game
    if (zombieKilled == zombieCount)
    {
        // victory
        cout << "You have survived the zombie war!" << endl;
    }
    else
    {
        // lost
        cout << "You did not survive the zombie war." << endl;
    }
    cout << "Zombies killed: " << zombieKilled << endl;
    cout << "Final score: " << playerScore << endl << endl;
}




