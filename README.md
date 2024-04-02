# LRU-Cache-realization

## About
This is a custom implementation of the data structure that follows the constraints of a Least Recently Used (LRU) cache. It supports basic operations of initialization, getting and putting elements.
***

## Realization

LRU Cache is a structure which stores pairs of key and values with limited capacity. When user adds element to full cache, least recently used item is discarded.

In the program it is represented as a structure with capacity, doubly linked list of elements and dictionary where keys are just the keys and values are references to appropriate elements.

Elements are represented as instances of the class Node, where key, value, next and previous Nodes are stored.

The functions get and put each run in O(1) average time complexity.
***

## Functionality

* The initialization function accepts only capacity and creates empty dictionary and doubly linked list (to store which we save pointers to beginning and end).

* The update function is an auxiliary function that is called in get and put in order to move an element which functions worked with to the end of a doubly linked list to store the order of usage.

* The get function accepts key and returns the value of the key if the key exists, otherwise returns -1. In the first case it also updates the element.

* The put function gets key and value. It changes the value of the key if the key exists. Otherwise, it adds the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, the least recently used key is evicted.
