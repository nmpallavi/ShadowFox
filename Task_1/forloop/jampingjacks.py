total = 100
done = 0

for i in range(10):  
    done += 10
    print(f"You have completed {done} jumping jacks.")
    
    if done < total:  
        tired = input("Are you tired? (yes/no): ").strip().lower()
        
        if tired in ["yes", "y"]:
            print(f"You completed a total of {done} jumping jacks.")
            break
        elif tired in ["no", "n"]:
            remaining = total - done
            print(f"{remaining} jumping jacks are remaining.")
    else:
        print("Congratulations! You completed the workout 🎉")
