import allAutoInvestCustom
import allDepositHistory
import binanceWalletValue
import privateWalletValue
import keys

epochTime = keys.get_epoch()

deposit_all = 0
deposit_all += allDepositHistory.getAllDeposit(keys.get_epoch_all_deposit())#ajouter l'epoch en variable d'entrée
deposit_all += allAutoInvestCustom.get_all_auto_invest(epochTime)

actual_value = 0
actual_value += binanceWalletValue.get_binance_wallet_value()
actual_value += privateWalletValue.get_private_wallet_value()

percentage = (actual_value/deposit_all - 1)*100
unrealised_gains = actual_value-deposit_all

print("Total deposit : ", deposit_all, ", Total Value : ", actual_value, ", Unrealised gains : ", unrealised_gains, ", ",percentage,"%")
