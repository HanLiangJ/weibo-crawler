
user_id_start=1669879400
user_id_end=1669879402
user_scale=[user_id_start, user_id_end]

def main():
    with open("user_id_list.txt","w") as file:
        for i in range(user_id_start, user_id_end):
            file.write(str(i))
            file.write('\n')



if __name__ == '__main__':
    main()