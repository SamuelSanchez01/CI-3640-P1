from Classes import *

programs = {} #Dictionary of programs
interpreters = {} #Dictionary of interpreters
translators = {} #Dictionary of translators
languages = ['LOCAL'] #Languages of the machine can run

#Main loop:
print("Bienvenido")
while True:
    userInput = input("$> ").split()
    if len(userInput) > 0:
        if userInput[0] == 'DEFINIR': #If the user want to define
            
            type = userInput[1]
            
            if type == "PROGRAMA": #If its a program
                if len(userInput) > 3:
                    name = userInput[2]
                    language = userInput[3]
                    if not language in languages:
                        languages.append(language)

                    if name not in programs:
                        programs[name] = Program(name, language)
                        if language not in languages:
                            languages.append(language)
                        print(f"Se definió el programa \'{name}\', ejecutable en \'{language}\'.")
                    else:
                        print(f"Error: El programa \'{name}\' ya está definido.")
                else:
                    print("Error: faltan argumentos.")

            elif type == "INTERPRETE": #If its an interpeter
                if len(userInput) > 2:
                    languageInter = userInput[2]
                    if languageInter not in languages:
                        languages.append(languageInter)

                    language = userInput[3]
                    if language not in languages:
                        languages.append(language)

                    if not language in interpreters:
                        interpreters[language] = [Interpreter(languageInter, language)]
                    else:
                        interpreters[language].append(Interpreter(languageInter, language) )
                    print(f"Se definió un intérprete para \'{language}\' escrito en \'{languageInter}\'.")
                else: 
                    print("Error: faltan argumentos.")

            elif type == "TRADUCTOR": #If its a translator
                if len(userInput) > 4:
                    languageTrans = userInput[2]
                    if languageTrans not in languages:
                        languages.append(languageTrans)

                    languageFrom = userInput[3]
                    if languageFrom not in languages:
                        languages.append(languageFrom)

                    languageTo = userInput[4]
                    if languageTo not in languages:
                        languages.append(languageTo)

                    if languageFrom in translators:
                        translators[languageFrom].append(Translator(languageTrans, languageFrom, languageTo))
                    else:
                        translators[languageFrom] = [Translator(languageTrans, languageFrom, languageTo)]
                    print(f"Se definió un traductor de \'{languageFrom}\' hacia \'{languageTo}\', escrito en \'{languageTrans}\'.")
                else:
                    print("Error: faltan argumentos.")
            else:
                print("Error: Solo se puede definir Traductor Intérprete o Porgrama.")

        elif userInput[0] == 'EJECUTABLE': #If the user want to know if he can execute

            if userInput[1] in programs:

                #Create the graph and check with the bfs if is executable
                vertices = {languages[i]: Vertex(languages[i], i) for i in range(len(languages))}
                g = Graph(list(vertices.values()))
                no_agregados = []

                for language in languages:
                    #Add of the interpreters as edges
                    if language in interpreters:
                        for interpreter in interpreters[language]:
                            g.addEdge(vertices[interpreter.language], vertices[interpreter.languageInter])

                    #Add of the translators as edges
                    if language in translators:
                        for traductor in translators[language]:
                            if g.BFS(vertices[traductor.languageTrans]):
                                g.addEdge(vertices[traductor.languageFrom], vertices[traductor.languageTo])
                            else:
                                no_agregados.append(traductor)
                        
                    #Check the translators that didnt was add cause it need for a interpreters
                    for traductor in no_agregados:
                        if g.BFS(vertices[traductor.languageTrans]):
                            g.addEdge(vertices[traductor.languageFrom], vertices[traductor.languageTo])
                            no_agregados.remove(traductor)

                #If exists a way printer
                if g.BFS(vertices[programs[userInput[1]].language]):
                    print(f"Si, es posible ejecutar el programa \'{userInput[1]}\'")
                #If there's no way
                else:
                    print(f"No es posible ejecutar el programa \'{userInput[1]}\'")

            else:
                print(f"El programa {userInput[1]} no existe en la maquina.")
        elif userInput[0] == 'SALIR':
            exit(0)
        else:
            print("Opción invalida. Los comandos válidos son: DEFINIR <type> [<argumentos>], EJECUTABLE <name>, SALIR")
    else:
        print("Manito pero pon un comando :(")