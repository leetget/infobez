package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	// Открываем файл
	file, err := os.Open("belka.txt")
	if err != nil {
		fmt.Println("Ошибка при открытии файла:", err)
		return
	}
	defer file.Close()

	// Создаем словарь для хранения частоты символов
	frequency := make(map[rune]int)

	// Считываем файл построчно
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		for _, char := range line {
			frequency[char]++
		}
	}

	// Проверяем на наличие ошибок при чтении файла
	if err := scanner.Err(); err != nil {
		fmt.Println("Ошибка при чтении файла:", err)
		return
	}

	// Выводим частоту символов
	fmt.Println("Частота встречающихся символов:")
	for char, count := range frequency {
		fmt.Printf("'%c': %d\n", char, count)
	}
}
