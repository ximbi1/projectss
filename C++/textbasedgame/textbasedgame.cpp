#include <iostream>
#include <string>
using namespace std;

// A struct to represent one "page" of the game.  IE:  a page is where
//  you print some text, then ask the user for input on what they want
//  to do next.
//
// Pages can lead to other pages, like a choose your own adventure book.
//
// Or pages can lead to a "game over"

struct Page
{
    string      text;           // the text displayed to the user when they're on this page

    int         options;        // the number of options available to the user.  If <= 0,
                                //   then this indicates the user has no options because
                                //   they died / got a game over.

    int         nextpage[10];   // The next page to go to depending on which option the user
                                //   selected.
};


/*
    THE DATA

    Here is where we'll have all of our pages defined.  Note we don't really have
    any code here... this is just data.  We're defining what the game world is...
    NOT how the game world works.

    (note that the way this is stored is not ideal -- but I'm just trying to show a
    conceptual example here)
*/

const Page gamePages[] = {
    ////////////////////////////////////////////
    // Page 0:  The start of the game
    {
        "Welcome to your adventure.  Which character would you like?\n"     // the flavor text
        "(1 for knight, 2 for samurai)\n",
        2,                              // number of options available to user
        {1,4}                           // if they choose option 1, go to page 1
                                        // if they choose option 2, go to page 4
    },

    ////////////////////////////////////////////
    // Page 1:  Knight selected
    {
		"You have chosen to become a knight.\n"     // flavor text
        "Welcome to the land known as Chronia.\n"
        "Their is a strangely dressed women. Do you approach her? (1 for y, 2 for n)\n",
        2,                              // 2 options
        {2,3}                           // option 1 -> page 2
                                        // option 2 -> page 3
    },

    ////////////////////////////////////////////
    // Page 2:  Knight selected, approaching woman
    {
        "You ask the women who she is and she replies I AM THE GREAT MICHELLINA\n"
        "How do I get back home? I DO NOT KNOW BUT IF YOU CAN GUESS IN WHICH HAND I HAVE THE ORB\n"
        "I WILL GET YOU BACK HOME. Which hand is it in? (1 for left, 2 for right)\n",
        2,
        {0,0}                           // TODO:  fill in your options here.  I have both options
                                        //  going back to page 0
    },

    ////////////////////////////////////////////
    // Page 3:  Knight selected, not approaching woman
    {
        "You do not approach her and get your head sliced off by an incoming horseman.\n"
        "Game Over. You suck at adventure games.",
        0,                      // 0 options because they got game over
        {}
    },

    ////////////////////////////////////////////
    // Page 4:  Samurai selected
    {
        "You have chose to become a samurai.\n"
        "Welcome to the land know as Remian.\n"
        "Their is another samurai charging at you. Do you attack them? (1 for y, 2 for n)\n",
        2,
        {5,0}       // option 1 -> page 5
                    // option 2 -> (TODO - fill in your next page... I have it going back to the start)
    },

    ////////////////////////////////////////////
    // Page 5:  Samurai selected, attacking other samurai
    {
        "The samurai head goes flying off and the horse bucks his body off and runs away scared.\n"
        "You search his body and find a key and a map to get back home.\n"
        "Do you want to get back home? (1 for y, 2 for n)\n",
        2,
        {0,0}       // TODO - fill in next pages
    }
};



/*
    THE CODE / LOGIC

    Now that we have all the game data set up... the code can use that data to actually drive the game.
*/

// the 'doPage' function will do the logic for the given 'page' parameter.
//   It will return the next page that the user will go to, or will return -1
//   if the user died / got game over.
int doPage(int page)
{
    // Page logic is simple:  output the flavor text
    cout << gamePages[page].text;

    // If the user has no options, they got game over
    if(gamePages[page].options <= 0)        // no options
        return -1;                          // return -1 to indicate game over

    // otherwise, if they did not get game over, get their selection
    int selection;
    cin >> selection;

    // make sure their selection is valid
    while(  selection < 1 ||                    // invalid selections are less than 1
            selection > gamePages[page].options // or are greater than the number of available options
         )
    {
        cout << "That is an invalid selection.  Please try again.\n";
        cin >> selection;
    }

    // their selection is valid.... so return the next page number to go to
    return gamePages[page].nextpage[ selection-1 ];  // note we have to subtract 1 here
                                                    // because our selection ID starts at 1
                                                    // but array indexes start at 0
}



/*
    MAIN

    Since doPage does all the logic, main is very simple.  It just keeps calling
    doPage until the user gets game over.
*/

int main()
{
    int currentPage = 0;        // start at page 0

    while(currentPage >= 0)     // as long as they don't have game over...
    {
        //... do a page
        currentPage = doPage(currentPage);
    }

    return 0;
}
