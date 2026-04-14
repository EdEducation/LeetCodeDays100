// попытка оптимизации на выделении памяти не сработала, 1 ms


/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2) {
        // Создаем фиктивный головной узел для упрощения кода (вернем dummyHead.next)
        ListNode dummyHead = new ListNode(0);
        ListNode current = dummyHead;
        int carry = 0; // перенос в следующий разряд
        
        // Оптимизация: используем ссылки напрямую, без дополнительных переменных в цикле
        // и проверяем существование узлов в условии цикла
        while (l1 != null || l2 != null)
        {
            // Суммируем значения и перенос
            int sum = carry;
            
            if (l1 != null)
            {
                sum += l1.val;
                l1 = l1.next; // перемещаем сразу после использования
            }
            
            if (l2 != null)
            {
                sum += l2.val;
                l2 = l2.next;
            }
            
            // Вычисляем цифру и новый перенос
            carry = sum / 10; // целочисленное деление работает быстрее
            current.next = new ListNode(sum % 10);
            current = current.next;
        }

        // Обрабатываем оставшийся перенос после цикла (отдельно для скорости)
        if (carry > 0)
        {
            current.next = new ListNode(carry);
        }
        
        return dummyHead.next;
    }
}