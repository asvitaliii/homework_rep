from tkinter import *
from tkinter import messagebox


# added comment
def main():

    handle = {'Иванов Иван Иванович': {'Должность': 'Стажер',
                                       'Кабинет': '001',
                                       'Телефон': '0123456789',
                                       'Почта': 'mail@gmail.com',
                                       'Cкайп': 'нету'}}

    window = Tk()
    window.title('Справочник предприятия')
    window.geometry('215x105')

    label1 = Label(window, text='Введите ФИО:')
    label1.grid(column=1, row=1)

    entry1 = Entry(window)
    entry1.grid(column=2, row=1)

    def search():
        nonlocal handle
        messagebox.showinfo(message=handle.get(entry1.get(), 'Не найдено!'))

    def add_info():
        window2 = Tk()
        window2.title('Ввод новых даных')
        window2.geometry('240x140')

        window2_label2 = Label(window2, text='Должность:')
        window2_label2.grid(column=1, row=2)
        window2_entry2 = Entry(window2)
        window2_entry2.grid(column=2, row=2)

        window2_label3 = Label(window2, text='Кабинет:')
        window2_label3.grid(column=1, row=3)
        window2_entry3 = Entry(window2)
        window2_entry3.grid(column=2, row=3)

        window2_label4 = Label(window2, text='Номер телефона:')
        window2_label4.grid(column=1, row=4)
        window2_entry4 = Entry(window2)
        window2_entry4.grid(column=2, row=4)

        window2_label5 = Label(window2, text='Почта:')
        window2_label5.grid(column=1, row=5)
        window2_entry5 = Entry(window2)
        window2_entry5.grid(column=2, row=5)

        window2_label6 = Label(window2, text='Скайп:')
        window2_label6.grid(column=1, row=6)
        window2_entry6 = Entry(window2)
        window2_entry6.grid(column=2, row=6)

        def writing_down():
            handle.update({entry1.get(): {'Должность': window2_entry2.get(),
                                          'Кабинет': window2_entry3.get(),
                                          'Телефон': window2_entry4.get(),
                                          'Почта': window2_entry5.get(),
                                          'Cкайп': window2_entry6.get()}})
            messagebox.showinfo(message='Запись сделана!')
            window2.destroy()

        window2_button = Button(window2, text='Сделать запись', command=writing_down)
        window2_button.grid(column=1, row=7, columnspan=2)

    def del_info():
        try:
            handle.pop(entry1.get())
            messagebox.showinfo(message='Даные удалены!')
        except KeyError:
            messagebox.showerror(title='Ошибка', message='Нету такой записи')

    button1 = Button(window, text='Поиск', command=search)
    button1.grid(column=1, row=3, columnspan=3)

    button2 = Button(window, text='Ввести новые даные', command=add_info)
    button2.grid(column=1, row=5, columnspan=3)

    button3 = Button(window, text='Удалить даные', command=del_info)
    button3.grid(column=1, row=7, columnspan=3)

    window.mainloop()


if __name__ == '__main__':
    main()
