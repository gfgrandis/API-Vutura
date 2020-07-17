from flask import Flask, request, jsonify

app = Flask(__name__)
checkout_db = []

@app.route('/keranjang', methods=['POST'])
def tambah_produk():
    data = request.get_json()
    checkout_db.append([data["nama_produk"], data["harga_produk"]])

    return jsonify({
        "chats": [
            {
                "text": "Produk telah ditambahkan",
                "type": "text"
            }
        ]
    })

@app.route('/keranjang', methods=['GET'])
def tampil_produk():
    nama_produk = []
    harga_produk = []
    isi_keranjang = []
    for x in checkout_db:
        nama_produk.append(x[0])
        harga_produk.append(int(x[1]))

    for i in range(len(nama_produk)):
        keranjang = "\nNama Produk: " + str(nama_produk[i]) + "\nHarga Produk: " + str("Rp{:,.2f}".format(harga_produk[i]))
        isi_keranjang.append(keranjang)

    return jsonify({
        "chats": [
            {
                "text": "Isi keranjang\n" + "\n".join(isi_keranjang),
                "type": "text"
            }
        ]
    })

@app.route('/pesanan', methods=['GET'])
def tampil_final_pesanan():
    harga_produk = []
    total_harga = 0
    for x in checkout_db:
        harga_produk.append(x[1])
        total_harga += int(x[1])

    return jsonify({
        "chats": [
            {
                "text": "Pembayaran \n\nTotal yang harus dibayarkan adalah : "+ str("Rp{:,.2f}".format(total_harga)) + "\n\nPembayaran bisa dilakukan melalui:\nRekening Monduri\n17515098715781917 Atasnama Galuh Fadillah",
                "type": "text"
            }
        ]
    })

if __name__ == '__main__':
    app.run(port=5000)
