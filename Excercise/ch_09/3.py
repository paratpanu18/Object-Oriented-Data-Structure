def insertion_sort(hand, remaining):
    if not remaining:
        print("sorted")
        print(hand)
        return

    def insert_recursively(index, element):
        if index == len(hand):
            hand.insert(index, element)
            if len(hand) > 1:
                print(f"insert {element} at index {index} : {hand} {remaining if remaining else ''}")
            return

        if hand[index] > element:
            hand.insert(index, element)
            if len(hand) > 1:
                print(f"insert {element} at index {index} : {hand} {remaining if remaining else ''}")
            return
        
        insert_recursively(index + 1, element)

    element_to_insert = remaining.pop(0)
    
    insert_recursively(0, element_to_insert)
    
    insertion_sort(hand, remaining)

hand = []
numbers = [int(i) for i in input("Enter Input : ").split()]
insertion_sort(hand, numbers)
