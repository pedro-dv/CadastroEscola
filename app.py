from escola import Escola
from alunos import Aluno
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class App:
    def __init__(self, nome: str):
        self.escola = Escola(nome)

        self.janela = Tk()
        self.janela.title(f"Sistema - {self.escola.nome}")

        # Label
        self.label_matricula = Label(self.janela, text="Matricula:",
                                     font="Tahoma 14 bold", fg="red")
        self.label_matricula.grid(row=0, column=0)

        # Entry
        self.txt_matricula = Entry(self.janela, font="Tahoma 14",
                                   width=27, state=DISABLED)
        self.txt_matricula.grid(row=0, column=1)

        # Label
        self.label_nome = Label(self.janela, text="Nome:",
                                font="Tahoma 14 bold", fg="red")
        self.label_nome.grid(row=1, column=0)

        # Entry
        self.txt_nome = Entry(self.janela, font="Tahoma 14",
                              width=27)
        self.txt_nome.grid(row=1, column=1)

        # Label
        self.label_idade = Label(self.janela, text="Idade:",
                                 font="Tahoma 14 bold", fg="red")
        self.label_idade.grid(row=2, column=0)

        # Entry
        self.txt_idade = Entry(self.janela, font="Tahoma 14",
                               width=27)
        self.txt_idade.grid(row=2, column=1)

        self.cursos = ['Python', 'Javascript', 'Node', 'Django']
        self.label_curso = Label(self.janela, text="Curso: ",
                                 font="Tahoma 14 bold", fg="red")
        self.label_curso.grid(row=3, column=0)

        # Combobox
        self.combo_cursos = ttk.Combobox(self.janela, values=self.cursos,
                                         width=25, state='readonly',
                                         font='Tahoma 14')
        self.combo_cursos.grid(row=3, column=1)

        # Label
        self.label_nota = Label(self.janela, text="Nota:",
                                font="Tahoma 14 bold", fg="red")
        self.label_nota.grid(row=4, column=0)

        # Entry
        self.txt_nota = Entry(self.janela, font="Tahoma 14",
                              width=27)
        self.txt_nota.grid(row=4, column=1)

        # BUTTONS
        self.button_adicionar = Button(self.janela, text="Adicionar",
                                       font="Tahoma 12 bold", width=7,
                                       fg="red", command=self.cadastrarAluno)
        self.button_adicionar.grid(row=5, column=0)

        self.button_editar = Button(self.janela, text="Editar",
                                    font="Tahoma 12 bold", width=7,
                                    fg="red", command=self.editarAluno)
        self.button_editar.grid(row=5, column=1)

        self.button_excluir = Button(self.janela, text="Excluir",
                                     font="Tahoma 12 bold", width=7,
                                     fg="red", command=self.deletarAluno)
        self.button_excluir.grid(row=5, column=2)

        # frame
        self.frame = Frame(self.janela)
        self.frame.grid(row=6, column=0, columnspan=3)

        self.colunas = ["Matricula", "Nome", "Idade", "Curso", "Nota"]
        self.tabela = ttk.Treeview(self.frame, columns=self.colunas, show="headings")
        for coluna in self.colunas:
            self.tabela.heading(coluna, text=coluna)
            self.tabela.column(coluna, width=110)

        self.tabela.bind("<ButtonRelease-1>", self.selecionarAluno)
        self.tabela.pack()

        self.atualizarTabela()
        self.janela.mainloop()

    def cadastrarAluno(self):
        nome = self.txt_nome.get()
        idade = int(self.txt_idade.get())
        curso = self.combo_cursos.get()
        nota = float(self.txt_nota.get())
        aluno = Aluno(nome, idade, curso, nota)

        self.escola.alunos.append(aluno)
        messagebox.showinfo("Sucesso!", "Aluno cadastrado com sucesso!")
        self.limparCampos()
        self.atualizarTabela()

    def limparCampos(self):
        self.txt_matricula.config(state=NORMAL)
        self.txt_matricula.delete(0, END)
        self.txt_matricula.config(state=DISABLED)
        self.txt_nome.delete(0, END)
        self.txt_idade.delete(0, END)
        self.combo_cursos.set('')
        self.txt_nota.delete(0, END)

    def atualizarTabela(self):
        for linha in self.tabela.get_children():
            self.tabela.delete(linha)

        for aluno in self.escola.alunos:
            self.tabela.insert("", END, values=(aluno.matricula,
                                                aluno.nome,
                                                aluno.idade,
                                                aluno.curso,
                                                aluno.nota))

    def selecionarAluno(self, event):
        linha_selecionada = self.tabela.selection()[0]
        valores = self.tabela.item(linha_selecionada)['values']
        self.limparCampos()
        self.txt_matricula.config(state=NORMAL)
        self.txt_matricula.insert(0, valores[0])
        self.txt_matricula.config(state=DISABLED)
        self.txt_nome.insert(0, valores[1])
        self.txt_idade.insert(0, valores[2])
        self.combo_cursos.set(valores[3])
        self.txt_nota.insert(0, valores[4])

    def deletarAluno(self):
        matricula = self.txt_matricula.get()
        opcao = messagebox.askyesno("Tem certeza?", "Deseja remover o aluno?")
        if opcao:
            self.escola.removerAluno(matricula)
            messagebox.showinfo("Sucesso!", "Aluno removido com sucesso!")
        self.limparCampos()
        self.atualizarTabela()


    def editarAluno(self):
        matricula = self.txt_matricula.get()
        nome = self.txt_nome.get()
        idade = int(self.txt_idade.get())
        nota = float(self.txt_nota.get())
        curso = self.combo_cursos.get()
        aluno = Aluno(nome, idade, curso, nota)
        aluno.matricula = matricula
        opcao = messagebox.askyesno('Tem certeza?', 'Deseja alterar os dados?')
        if opcao:
            self.escola.editarAluno(aluno)
            messagebox.showinfo('Sucesso!', 'Dados alterado com sucesso!')
        self.limparCampos()
        self.atualizarTabela()







App("Infinity")
