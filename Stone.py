
#include <stdio.h>
#include <stdlib.h>
int main()
{
    int no_of_piles,stones_in_piles,counter1,counter2;
    int player,first_chance,no_of_testcases;
    int winner;
    scanf("%d",&no_of_testcases);
    winner = (int )malloc(sizeof(int) no_of_testcases);
    for(counter2=0;counter2<no_of_testcases;counter2++)
    {
        player = 1;//1 = Alice , 0 = Bob
        first_chance = 1;
        scanf("\n%d",&no_of_piles);
        stones_in_piles = (int )malloc(sizeof(int) no_of_piles);
        for(counter1=0;counter1<no_of_piles;counter1++)
            { 
            scanf("%d",&stones_in_piles[counter1]);
            }
        while(1)
        {
        for(counter1=0;counter1<no_of_piles;counter1++)
        {
        if(stones_in_piles[counter1]>=(counter1+1))
        {
        stones_in_piles[counter1]=stones_in_piles[counter1]-(counter1+1);
        if(player)
        player = 0;
        else
        player = 1;
        first_chance = 0;
        break;
        }
        }
        if(counter1 == no_of_piles)
        {
        if(first_chance)
        {
        printf("\nNo one wins as no piles sufficient to play");
        free(stones_in_piles);
        break;
        }
        if(player)
        player = 0;
        else
        player = 1;
        winner[counter2]=player;
        free(stones_in_piles);
        break;
        }
        }
        }
        for(counter2=0;counter2<no_of_testcases;counter2++)
        {
            if(winner[counter2])
            printf("Alice\n");
            else
            printf("Bob\n");
    
    }
    free(winner);
}