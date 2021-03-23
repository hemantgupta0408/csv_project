import pandas as pd

df1 = pd.read_csv('hotels.csv', index_col ='Sr. No.')

if __name__ == "__main__":
    r = 'Ratings'
    c = 'Cost'
    print("----- Select state from Karnataka/Tamilnadu/Maharashtra or india also -----")
    state = input("What is the state :").lower()
    if state == "karnataka":
        df2 = df1.State.str.contains("Karnataka")
        karnataka = df1[df2]
        cr = input("Cost or Rating:").lower()
        if cr == "rating":
            cr = karnataka.Ratings
            op = input("Operation:").lower()
            if op == "cheapest":
                minimum = cr.min()
                new = karnataka[karnataka[r] == minimum ].iloc[1]
                print(f"Hotel with {op} rating in {state} is {new['Hotel Code']} with rating {new['Ratings']}")

            elif op == "highest":
                maximum = cr.max()
                new = karnataka[karnataka[r] == maximum ].iloc[1]
                print(f"Hotel with {op} rating in {state} is {new['Hotel Code']} with rating {new['Ratings']}")
                

            elif op == "average":
                avg = cr.mean()
                print(f"{op} rating of Hotel in {state} is {avg}")

            else:
                print("you enter wrong input....")

        elif cr == "cost":
            cr = karnataka.Cost
            op = input("Operation:").lower()
            if op == "cheapest":
                minimum = cr.min()
                new = karnataka[karnataka[c] == minimum ].iloc[1]
                print(f"Hotel with {op} price in {state} is {new['Hotel Code']} with price {new['Cost']}")

            elif op == "highest":
                maximum = cr.max()
                new = karnataka[karnataka[c] == maximum ].iloc[1]
                print(f"Hotel with {op} price in {state} is {new['Hotel Code']} with price {new['Cost']}")

            elif op == "average":
                avg = cr.mean()
                print(f"{op} cost of Hotel in {state} is {avg}")

            else:
                print("you enter wrong input....")

    elif state == "tamilnadu":
        df2 = df1.State.str.contains("Tamilnadu")
        tamilnadu = df1[df2]
        cr = input("Cost or Rating:").lower()
        if cr == "rating":
            cr = tamilnadu.Ratings
            op = input("Operation:").lower()
            if op == "cheapest":
                minimum = cr.min()
                new = tamilnadu[tamilnadu[r] == minimum ].iloc[1]
                print(f"Hotel with {op} rating in {state} is {new['Hotel Code']} with rating {new['Ratings']}")

            elif op == "highest":
                maximum = cr.max()
                new = tamilnadu[tamilnadu[r] == maximum ].iloc[1]
                print(f"Hotel with {op} rating in {state} is {new['Hotel Code']} with rating {new['Ratings']}")

            elif op == "average":
                avg = cr.mean()
                print(f"{op} rating of Hotel in {state} is {avg}")

            else:
                print("you enter wrong input....")

        elif cr == "cost":
            cr = tamilnadu.Cost
            op = input("Operation:").lower()
            if op == "cheapest":
                minimum = cr.min()
                new = tamilnadu[tamilnadu[c] == minimum ].iloc[1]
                print(f"Hotel with {op} price in {state} is {new['Hotel Code']} with price {new['Cost']}")

            elif op == "highest":
                maximum = cr.max()
                new = tamilnadu[tamilnadu[c] == maximum ].iloc[1]
                print(f"Hotel with {op} price in {state} is {new['Hotel Code']} with price {new['Cost']}")

            elif op == "average":
                avg = cr.mean()
                print(f"{op} cost of Hotel in {state} is {avg}")

            else:
                print("you enter wrong input....")

        else:
            print("you enter wrong input....")

    elif state == "maharashtra":
        df2 = df1.State.str.contains("Maharashtra")
        maharashtra = df1[df2]
        cr = input("Cost or Rating:").lower()
        if cr == "rating":
            cr = maharashtra.Ratings
            op = input("Operation:").lower()
            if op == "cheapest":
                minimum = cr.min()
                new = maharashtra[maharashtra[r] == minimum ].iloc[1]
                print(f"Hotel with {op} rating in {state} is {new['Hotel Code']} with rating {new['Ratings']}")

            elif op == "highest":
                maximum = cr.max()
                new = maharashtra[maharashtra[r] == maximum ].iloc[1]
                print(f"Hotel with {op} rating in {state} is {new['Hotel Code']} with rating {new['Ratings']}")

            elif op == "average":
                avg = cr.mean()
                print(f"{op} rating of Hotel in {state} is {avg}")

            else:
                print("you enter wrong input....")

        elif cr == "cost":
            cr = maharashtra.Cost
            op = input("Operation:").lower()
            if op == "cheapest":
                minimum = cr.min()
                new = maharashtra[maharashtra[c] == minimum ].iloc[1]
                print(f"Hotel with {op} price in {state} is {new['Hotel Code']} with price {new['Cost']}")

            elif op == "highest":
                maximum = cr.max()
                new = maharashtra[maharashtra[c] == maximum ].iloc[1]
                print(f"Hotel with {op} price in {state} is {new['Hotel Code']} with price {new['Cost']}")

            elif op == "average":
                avg = cr.mean()
                print(f"{op} cost of Hotel in {state} is {avg}")

    elif state == "india":
        india = df1
        cr = input("Cost or Rating:").lower()
        if cr == "rating":
            cr = india.Ratings
            op = input("Operation:").lower()
            if op == "cheapest":
                minimum = cr.min()
                new = india[india[r] == minimum ].iloc[1]
                print(f"Hotel with {op} rating in {new['State']} is {new['Hotel Code']} with price {new['Ratings']}")
                                      
            elif op == "highest":
                maximum = cr.max()
                new = india[india[r] == maximum ].iloc[1]
                print(f"Hotel with {op} rating in {new['State']} is {new['Hotel Code']} with price {new['Ratings']}")
                
            elif op == "average":
                avg = cr.mean()
                print(f"{op} rating of hotel in {state} is {avg}")               

            else:
                print("you enter wrong input....")
            
        elif cr == "cost":
            cr = india.Cost
            op = input("Operation:").lower()
            if op == "cheapest":
                minimum = cr.min()
                new = india[india[c] == minimum ].iloc[1]
                print(f"Hotel with {op} price in {new['State']} is {new['Hotel Code']} with price {new['Cost']}")
                                     
            elif op == "highest":
                maximum = cr.max()
                new = india[india[c] == maximum ].iloc[1]
                print(f"Hotel with {op} price in {new['State']} is {new['Hotel Code']} with price {new['Cost']}")
                
            elif op == "average":
                avg = cr.mean()
                print(f"{op} price of hotel in {state} is {avg}")
                
            else:
                print("wrong input....")

    else:
        print("wrong input....")
