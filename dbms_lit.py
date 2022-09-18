import streamlit as st
#print("TRC TO SQL")
st.write("TRC TO SQL")

def singletable() : 
    st.write("\nUse only One Table")
    st.write("Enter TRC in form {t|P(t)} ")
    st.write("Available Comparision Operators : <, <=, =, !=, >, >= \nAvailable Connectives : and(^), or(V)\n")
    trc = st.text_input("Enter The TRC : ")
    trc = trc.strip("{}")
    st.write("\nSplitting TRC : ",trc)
    sub = trc

    st.write("Number of '^' : ",trc.count("^"))
    if "t e" in trc :
        if "^" not in trc :
           st.write("\nSQL Query : Select * from",trc[6:])
        else:
            ind = trc.index("t.")
            ind = ind + 2
            st.write("Index of Column Name : ",ind)
            #finding table name
            table = trc[6:trc.index("^")]
            if trc.count("^")==1 and trc.count("V")==0 :
                st.write("\nSQL Query : Select * from ",table,"where",trc[ind:])
            else:
                if trc.count("V")==0 :
                    temp = trc[(trc.index("^")+2):]
                    st.write("Extracting TRC after first '^' : ",temp)
                    #print("hi")
                    ind = temp.index("t.")
                    ind = ind + 2
                    st.write("\nSQL Query : Select * from ",table,"where",temp[ind:temp.index("^")],end="")

                    while temp.count("^") !=0 :
                        temp = temp[(temp.index("^")+2):]
                        ind = temp.index("t.")
                        ind = ind + 2
                        if temp.count("^") < 1 :
                            st.write("and",temp[ind:],end="")
                        else:
                            st.write("and",temp[ind:temp.index("^")],end="")
                elif trc.count("V") != 0 :
                    ind = trc.index("t.")
                    ind = ind + 2
                    #print("his")
                    temp = trc[(trc.index("^")+2):]
                    st.write("Extracting TRC after first '^' : ",temp)
                    ind = temp.index("t.")
                    ind = ind + 2
                    st.write("\nSQL Query : Select * from ",table,"where",temp[ind:temp.index("V")],end=" ")

                    while temp.count("V") !=0 :
                        temp = temp[(temp.index("V")+2):]
                        ind = temp.index("t.")
                        ind = ind + 2
                        if temp.count("V") < 1 :
                            st.write("or",temp[ind:],end="")
                        else:
                            st.write("or",temp[ind:temp.index("V")],end="")
    st.write("\n\n")

def twotables() : 
    st.write("Enter TRC in form {t|t e 'table name' ^ ......^(...)} ")
    st.write("Available Comparision Operators : <, <=, =, !=, >, >= \nAvailable Connectives : and(^)\n")
    trc = st.text_input("Enter The TRC : ")
    trc = trc.strip("{}")
    st.write("\nAfter Splitting : ",trc)
    sub = trc
    str = "*"
    tstr = ""
    lst = []
    lst1 = []
    lst2 = []

    tind = trc.index("(")
    s = trc[:trc.index("(")]
    temp3 = trc[tind:]
    temp3 = temp3.strip("(")
    temp3 = temp3.strip(")")
    #printing temp3
    st.write("\nData inside ( ) : ",temp3)
    table = trc[6:trc.index("^")]
    
    if "s e" in trc :
        ind = (s.index("s."))
        temp = s[ind:]
        #printing temp
        st.write("\nData outside ( ) and within { } : ",temp)
        while temp.count("s.")!=0 :
            #print(temp)
            ind = (temp.index("s."))
            if "^" not in temp :
                #print("1::",temp[(ind+2):])
                lst.append(temp[(ind+2):])
                break
            else:
                lst.append(temp[(ind+2):temp.index("^")])
                st.write("Extracting Column Name : ",temp[(ind+2):temp.index("^")])
                st.write(temp)
                ind = (temp.index("^")+1)
                st.write(ind)
                temp = temp[ind:]
                
    if "s e" in trc:
        st.write("List of Columns : ",lst)
        for x in lst:
            if x == lst[0]:
                tstr = x
            else:
                tstr = tstr + "," + x
        str = tstr
        
    if "s e" in trc :
        if "^" not in trc :
            st.write("\nSQL Query : Select",str,"from",trc[6:])
        else:
            ind = temp3.index("s.")
            ind = ind + 2
            st.write("--",ind)
            #finding table name
            table = trc[6:trc.index("^")]
            if temp3.count("^") == 0 and temp3.count("V") == 0 :
                st.write("\nSQL Query : Select",str,"from",table,"where",temp3[ind:])
            else:
                if temp3.count("V")==0 :
                    #temp = temp3[(temp3.index("^")+2):]
                    temp = temp3[2 : ]
                    st.write("--",temp)
                    #print("hi")
                    st.write("\nSQL Query : Select",str,"from",table,"where",temp[:temp.index("^")],end="")
                
                    while temp.count("^") != 0 :
                        temp = temp[(temp.index("^")+2):]
                        ind = temp.index("s.")
                        ind = ind + 2
                        if temp.count("^") < 1 :
                            st.write("and",temp[ind:],end="")
                        else:
                            st.write("and",temp[ind:temp.index("^")],end="")
                elif temp3.count("V") != 0 :
                    ind = temp3.index("s.")
                    ind = ind + 2
                    #print("his")
                    #temp = trc[(trc.index("^")+2):]
                    temp = temp3[2 : ]
                    st.write("--",temp)
                    ind = temp.index("s.")
                    ind = ind + 2
                    st.write("\nSQL Query : Select",str,"from ",table,"where",temp[ind:temp.index("V")],end=" ")

                    while temp.count("V") != 0 :
                        temp = temp[(temp.index("V")+2):]
                        ind = temp.index("s.")
                        ind = ind + 2
                        if temp.count("V") < 1 :
                            st.write("or",temp[ind:],end="")
                        else:
                           st.write("or",temp[ind:temp.index("V")],end="")

    if "t e" in trc :
        if "^" not in trc :
            st.write("\nSQL Query : Select * from",trc[6:])
        else:
            ind = trc.index("t.")
            ind = ind + 2
            st.write("--",ind)
            #finding table name
            table = trc[6:trc.index("^")]
            if trc.count("^")==1 and trc.count("v")==0 :
                st.write("\nSQL Query : Select * from ",table,"where",trc[ind:])
            else:
                if trc.count("V")==0 :
                    temp = trc[(trc.index("^")+2):]
                    st.write("--",temp)
                    #print("hi")
                    ind = temp.index("t.")
                    ind = ind + 2
                    st.write("\nSQL Query : Select * from ",table,"where",temp[ind:temp.index("^")],end="")

                    while temp.count("^") !=0 :
                        temp = temp[(temp.index("^")+2):]
                        ind = temp.index("t.")
                        ind = ind + 2
                        if temp.count("^") < 1 :
                            st.write("and",temp[ind:],end="")
                        else:
                            st.write("and",temp[ind:temp.index("^")],end="")
                elif trc.count("V") != 0 :
                    ind = trc.index("t.")
                    ind = ind + 2
                    #print("his")
                    temp = trc[(trc.index("^")+2):]
                    st.write("--",temp)
                    ind = temp.index("t.")
                    ind = ind + 2
                    st.write("\nSQL Query : Select * from ",table,"where",temp[ind:temp.index("V")],end=" ")

                    while temp.count("V") !=0 :
                        temp = temp[(temp.index("V")+2):]
                        ind = temp.index("t.")
                        ind = ind + 2
                        if temp.count("V") < 1 :
                            st.write("or",temp[ind:],end="")
                        else:
                            st.write("or",temp[ind:temp.index("V")],end="")
    st.write("\n\n")   

st.write("Tuple Relational Calculus To SQL Query Converter\n")
ans = True 
while ans : 
    st.write("1.TRC with one table(t) \n2.TRC with two tables(t,s) \n3.Exit")
    ans = st.number_input("Enter number corresponding to operation you wish to perform : \n")
    if ans == 1 : 
        singletable()
    elif ans == 2 : 
        twotables()
    elif ans == 3 : 
        ans = False
        st.write("Thank you for using the converter!!")
    else : 
        st.write("Please Enter Valid Number")
        
st.write("\n")