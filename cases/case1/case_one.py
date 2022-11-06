from datetime import date, timedelta


class CaseOne:

    @staticmethod
    def filter_by_date_company_value_description(transaction, args):
        return list(filter(lambda x: x[0] == args[0] and x[1] == args[1] and x[2] == args[2] and x[3] == args[3],
                           transaction))

    @staticmethod
    def check_missing_transactions(transaction):
        return list(filter(lambda x: len(x) == 4, transaction))

    @staticmethod
    def locate_transaction(results, transaction):
        for result in results:
            if len(result) == 5:
                continue
            transaction.append('FOUND')
            result.append('FOUND')
            return True
        return False

    def reconcile_accounts(self, transactions1: list[list], transactions2: list[list]):
        """
            Objetivo
            - Validar as listas e acrescentar uma nova coluna indicando o status da transação[FOUND, MISSING]
            Regras
            - Pode existir transações duplicadas, nesse caso cada transação deve ter um relacionamento 1 pra 1
            - Quando houver mais de uma possibilidade de correspondencia para uma data transação, deve se considerar
              a que ocorreu mais cedo.
            - Cada transação pode corresponder a uma transação que seja do dia anterior ou posterior, desde que
              contenham as demais colunas com o mesmo valor.
        """
        transactions1.sort()
        transactions2.sort()
        for transaction in transactions1:
            results = self.filter_by_date_company_value_description(transactions2, transaction)
            if not self.locate_transaction(results, transaction):
                transaction_date = date.fromisoformat(transaction[0])
                copy_transaction = transaction.copy()
                day_after = transaction_date + timedelta(1)
                copy_transaction[0] = str(day_after)
                results = self.filter_by_date_company_value_description(transactions2, copy_transaction)
                if not self.locate_transaction(results, transaction):
                    day_before = transaction_date - timedelta(1)
                    copy_transaction[0] = str(day_before)
                    results = self.filter_by_date_company_value_description(transactions2, copy_transaction)
                    self.locate_transaction(results, transaction)

        for transaction in self.check_missing_transactions(transactions1):
            transaction.append('MISSING')

        for transaction in self.check_missing_transactions(transactions2):
            transaction.append('MISSING')

        return transactions1, transactions2
