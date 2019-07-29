import time
class SudokuSolver:
    ###  Defining Functions  ###
    subtract_set = {1,2,3,4,5,6,7,8,9}
    def __init__(self, container):
        self.container=container

    def check_horizontal(self,i,j):
        return self.subtract_set - set(self.container[i])

    def check_vertical(self,i,j):
        ret_set = []
        for x in range(9):
            ret_set.append(self.container[x][j])
        return self.subtract_set - set(ret_set)

    def check_square(self,i,j):
        first = [0,1,2]
        second = [3,4,5]
        third = [6,7,8]
        find_square = [first,second,third]
        for l in find_square:
            if i in l:
                row = l
            if j in l:
                col = l
        ret_set = []
        for x in row:
            for y in col:
                ret_set.append(self.container[x][y])
        return self.subtract_set - set(ret_set)

    def get_poss_vals(self,i,j):
        poss_vals = list(self.check_square(i,j).intersection(self.check_horizontal(i,j)).intersection(self.check_vertical(i,j)))
        return poss_vals

    def explicit_solver(self,container):
        stump_count = 1
        for i in range(9):
            for j in range(9):
                if container[i][j] == 0:
                    poss_vals = self.get_poss_vals(i,j)
                    if len(poss_vals) == 1:
                        container[i][j] = list(poss_vals)[0]
                        # print_container(container)
                        stump_count = 0
        return container, stump_count

    def implicit_solver(self,i,j,container):
        if container[i][j] == 0:
            poss_vals = self.get_poss_vals(i,j)
            
            #check row
            row_poss = []
            for y in range(9):
                if y == j:
                    continue
                if container[i][y] == 0:
                    for val in self.get_poss_vals(i,y):
                        row_poss.append(val)
            if len(set(poss_vals)-set(row_poss)) == 1:
                container[i][j] = list(set(poss_vals)-set(row_poss))[0]
                # print_container(container)
            
            #check column
            col_poss = []
            for x in range(9):
                if x == i:
                    continue
                if container[x][j] == 0:
                    for val in self.get_poss_vals(x,j):
                        col_poss.append(val)
            if len(set(poss_vals)-set(col_poss)) == 1:
                container[i][j] = list(set(poss_vals)-set(col_poss))[0]
                # print_container(container)
                    
            #check square
            first = [0,1,2]
            second = [3,4,5]
            third = [6,7,8]
            find_square = [first,second,third]
            for l in find_square:
                if i in l:
                    row = l
                if j in l:
                    col = l
            square_poss = []
            for x in row:
                for y in col:
                    if container[x][y] == 0:
                        for val in self.get_poss_vals(x,y):
                            square_poss.append(val)
            if len(set(poss_vals)-set(square_poss)) == 1:
                container[i][j] = list(set(poss_vals)-set(square_poss))[0]
                # print_container(container)
        return container

    def print_container(self,container):
        for i, row in enumerate(container):
            for j, val in enumerate(row):
                if (j)%3 == 0 and j<8 and j>0:
                    print("|",end=' ')
                print(val,end=' ')
            print()
            if (i-2)%3 == 0 and i<8:
                print("_____________________", end='')
                print()
            print()
        print()
        print("||||||||||||||||||||||")
        print()
    def validate_solved(self):
        pass
    def check_solved(container):
        zero_count = 0
        for l in container:
            for v in l:
                if v == 0:
                    zero_count += 1
        return zero_count

    def solve(self):
        # using explicit solver
        start = time.time()
                    
        # print(f'There are {check_solved(self.container)} moves I have to make!')
        # print()

        # print_container(container)
        # print()
        solving = True

        while solving:
            #Solver Portion
            container, stump_count = self.explicit_solver(self.container)
            
            #Loop-Breaking Portion
            zero_count = 0
            for l in container:
                for v in l:
                    if v == 0:
                        zero_count += 1
            if zero_count==0:
#                 print_container(container)
                solving=False
            if stump_count > 0:
                for i in range(9):
                    for j in range(9):
                        container = self.implicit_solver(i,j,container)
        # print()
        # print('That took', time.time()-start, 'seconds!')
        # self.print_container(self.container)
        return self.container


# container = []
# container.append([0,0,0,0,0,8,3,0,0])
# container.append([0,0,0,0,2,4,0,9,0])
# container.append([0,0,4,0,7,0,0,0,6])
# container.append([0,0,0,0,0,3,0,7,9])
# container.append([7,5,0,0,0,0,0,8,4])
# container.append([9,2,0,5,0,0,0,0,0])
# container.append([4,0,0,0,9,0,1,0,0])
# container.append([0,3,0,4,6,0,0,0,0])
# container.append([0,0,5,8,0,0,0,0,0])
# ss=SudokuSolver(container)
# ss.solve()