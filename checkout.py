from flask import Flask, request, jsonify

app = Flask(__name__)
pesanan = {}

produk = {
  "Mac":
      { "list_barang" : [
    {
      "id": 1,
      "nama_produk": "Macbook Air",
      "harga_produk": 15000000,
      "promo" : True,
      "url_img": "https://cdn.mos.cms.futurecdn.net/TaicKGcS88HAJ9eHtx6JwH-970-80.jpg",
      "stok" : 10
    },
    {
      "id": 2,
      "nama_produk": "Macbook Pro",
      "harga_produk": 30000000,
      "promo": False,
      "url_img": "https://sm.pcmag.com/t/pcmag_ap/review/a/apple-macb/apple-macbook-pro-16-inch_e1zs.640.jpg",
      "stok" : 20
    },
    {
      "id": 3,
      "nama_produk": "iMac",
      "harga_produk": 20000000,
      "promo": False,
      "url_img": "https://ibox.co.id/media/catalog/product/cache/3/image/9df78eab33525d08d6e5fb8d27136e95/i/m/imac-27-cto-hero-201903_1_1.jpeg",
      "stok" : 50
    }
  ],
      "url_img" : "https://storage.googleapis.com/vutura/assets/images/b9e02c0c-5a12-4740-9280-2774a9c61598.jpg",
      "keterangan" : "Silahkan klik tombol di bawah untuk mencari produk Mac yang sesuai"},
  "iPad":
      { "list_barang" : [
    {
      "id": 1,
      "nama_produk": "iPad Air 2019",
      "harga_produk": 8000000,
      "promo": False,
      "url_img": "https://www.gizmochina.com/wp-content/uploads/2019/03/Apple-iPad-Air-2019-500x500.jpg",
      "stok" : 10
    },
    {
      "id": 2,
      "nama_produk": "iPad 7",
      "harga_produk": 5000000,
      "promo" : True,
      "url_img": "https://s.blanja.com/picspace/56/305208/700.462_e3cc17e2d3ae4faa8102dcb0435bba35.jpg",
      "stok" : 20
    },
    {
      "id": 3,
      "nama_produk": "iPad Pro",
      "harga_produk": 20000000,
      "promo": False,
      "url_img": "https://icdn3.digitaltrends.com/image/digitaltrends/ipad-pro-2018-review-5848-768x479-c.jpg",
      "stok" : 50
    }
  ],
      "url_img" : "https://i.pcmag.com/imagery/reviews/04Pl0gzG2hLLGkonGAsUMmb-12..v_1574731296.jpg",
      "keterangan" : "Silahkan klik tombol di bawah untuk mencari tablet iPad yang sesuai"},
"iPhone":
      { "list_barang" : [
    {
      "id": 1,
      "nama_produk": "iPhone XR",
      "harga_produk": 10000000,
      "promo" : True,
      "url_img": "https://p.ipricegroup.com/uploaded_a545ecc174943263565ec786c03b9fdf.jpg",
      "stok" : 10
    },
    {
      "id": 2,
      "nama_produk": "iPhone 11",
      "harga_produk": 10000000,
      "promo": False,
      "url_img": "https://id-test-11.slatic.net/p/abbbe4a6e24b6658229755b18352e254.jpg",
      "stok" : 20
    },
    {
      "id": 3,
      "nama_produk": "iPhone 11 Pro",
      "harga_produk": 15000000,
      "promo": False,
      "url_img": "https://p.ipricegroup.com/uploaded_df23273ab706197931c6092e3b2b40e5.jpg",
      "stok" : 50
    }
  ],
      "url_img" : "https://cdn.vox-cdn.com/thumbor/MwokWf8IUu77WSTyqnrzfHfrWew=/0x146:2040x1214/fit-in/1200x630/cdn.vox-cdn.com/uploads/chorus_asset/file/19206380/akrales_190913_3666_0391.jpg",
      "keterangan" : "Silahkan klik tombol di bawah untuk mencari smartphone iPhone yang sesuai"}
}

data_keranjang = {

}


@app.route('/<kategori>')
def tampil_produk(kategori):
    kolom = []
    for i in range(len(produk[kategori]["list_barang"])):
        lagi_promo = ""
        if produk[kategori]["list_barang"][i]["promo"]:
            lagi_promo = "BARANG SEDANG PROMO"
        if produk[kategori]["list_barang"][i]["stok"] > 0:
            info_produk = {
                "title": produk[kategori]["list_barang"][i]["nama_produk"],
                "text": "Rp{:,.2f}".format(produk[kategori]["list_barang"][i]["harga_produk"]) + "\nStok :" + str(produk[kategori]["list_barang"][i]["stok"]) + "\n" + lagi_promo,
                "image_url": produk[kategori]["list_barang"][i]["url_img"],
                "buttons": [
                {
                    "label": "Beli",
                    "type": "path",
                    "path": "5ed9ebd020f8374bf65abbe6",
                    "variable": {
                        "nama_produk": produk[kategori]["list_barang"][i]["nama_produk"],
                        "harga_produk": str(produk[kategori]["list_barang"][i]["harga_produk"]),
                        "url_img" : produk[kategori]["list_barang"][i]["url_img"]
                    }
                },
                {
                    "label": "Kembali",
                    "type": "path",
                    "path": "5ed5f3ac20f8374bf65aa6a5"
                }
                ],
                "type": "button"
            }
            kolom.append(info_produk)


    return jsonify({
        "chats": [
            {
                "columns": kolom,
                "type": "carousel"
            }
        ]
        })

@app.route('/promo')
def tampil_promo():
    kolom = []
    for kategori in produk:
        for barang in produk[kategori]["list_barang"]:
            lagi_promo = ""
            if barang["promo"]:
                lagi_promo = "BARANG SEDANG PROMO"
            if barang["stok"] > 0 and barang["promo"]:
                info_produk = {
                    "title": barang["nama_produk"],
                    "text": "Rp{:,.2f}".format(barang["harga_produk"]) + "\nStok :" + str(barang["stok"]) + "\n" + lagi_promo,
                    "image_url": barang["url_img"],
                    "buttons": [
                        {
                            "label": "Beli",
                            "type": "path",
                            "path": "5ed9ebd020f8374bf65abbe6",
                            "variable": {
                                "nama_produk": barang["nama_produk"],
                                "harga_produk": str(barang["harga_produk"]),
                                "url_img" : barang["url_img"]
                            }
                        },
                        {
                            "label": "Kembali",
                            "type": "path",
                            "path": "5ed5f3ac20f8374bf65aa6a5"
                        }
                    ],
                    "type": "button"
                }
                kolom.append(info_produk)

    return jsonify({
        "chats": [
            {
                "columns": kolom,
                "type": "carousel"
            }
        ]
    })

@app.route('/kategori')
def tampil_kategori():
    kolom = []
    for kategori in produk:
        stok = 0
        print(kategori)
        for barang in produk[kategori]["list_barang"]:
            stok += barang["stok"]
        if stok > 0:
            info_produk = {
                "title": kategori,
                "text": produk[kategori]["keterangan"],
                "image_url": produk[kategori]["url_img"],
                "buttons": [
                    {
                        "label": "Cari",
                        "type": "path",
                        "path": "5ee0868b20f837185ebed1a4",
                        "variable": {
                            "kategori": kategori
                        }
                    },
                    {
                        "label": "Kembali",
                        "type": "path",
                        "path": "5ed5b85920f8374bf65aa244" #ke menu greeting
                    }
                ],
                "type": "button"
            }
            kolom.append(info_produk)

    return jsonify({
        "chats": [
            {
                "columns": kolom,
                "type": "carousel"
            }
        ]
    })

@app.route('/keranjang')
def tampil_keranjang():
    if len(data_keranjang)==0:
        return jsonify({
            "chats": [
                {
                    "text" : "Keranjang belanja anda masih kosong",
                    "type" : "text"
                }
            ]
        })
    else:
        listkeranjang = ""
        totalharga = 0
        for produk in data_keranjang:
            listkeranjang = listkeranjang+str(produk)+" - "+str("Rp{:,.2f}".format(data_keranjang[produk]["harga"]))+" Jumlah:"+str(data_keranjang[produk]["jumlah"])+"\n" #jumlahnya kadang suka ga tentu
            totalharga = totalharga+ (data_keranjang[produk]["harga"]*data_keranjang[produk]["jumlah"])
        return jsonify({
            "chats": [
                {
                    "text" : str(listkeranjang) + "\nTotal belanja kamu adalah "+str("Rp{:,.2f}".format(totalharga)),
                    "type" : "text"
                }
            ]
        })

@app.route('/carousel_keranjang')
def carousel_keranjang():
    kolom = []
    for produk in data_keranjang:
        info_produk = {
            "title": str(produk),
            "text": "Rp{:,.2f}".format(data_keranjang[produk]["harga"]) + "\nJumlah :" + str(data_keranjang[produk]["jumlah"]),
            "image_url": data_keranjang[produk]["url"],
            "buttons": [
                {
                    "label": "Hapus Produk",
                    "type": "path",
                    "path": "5ee09a4e20f837185ebed3a3",
                    "variable": {
                        "nama_produk": produk
                    }
                },
                {
                    "label": "Ubah Jumlah",
                    "type": "path",
                    "path": "5ee09c9420f837185ebed3d5",
                    "variable": {
                        "nama_produk": produk
                    }
                },
                {
                    "label": "Kembali",
                    "type": "path",
                    "path": "5ed6082520f8374bf65aa742"
                }
            ],
            "type": "button"
        }
        kolom.append(info_produk)

    return jsonify({
        "chats": [
            {
                "columns": kolom,
                "type": "carousel"
            }
        ]
    })

@app.route('/keranjang/hapus', methods=['POST'])
##contoh bentuk body request {"nama" : "Macbook Air"}
def hapus_keranjang():
    hapus_produk = request.json['nama']
    # I.S : Produk sudah ada di keranjang
    for kategori in produk:
        for barang in produk[kategori]["list_barang"]:
            if barang["nama_produk"] == hapus_produk:
                barang["stok"] += data_keranjang[hapus_produk]["jumlah"]
    del data_keranjang[hapus_produk]
    return jsonify({"data_keranjang" : data_keranjang})

@app.route('/keranjang/ubah', methods=['POST'])
##contoh bentuk body request {"nama" : "Macbook Air", "jumlah" : "3"}
def ubah_keranjang():
    hapus_produk = request.json['nama']
    jumlah_ubah = int(request.json['jumlah'])
    # I.S : Produk sudah ada di keranjang
    stok_barang = 0
    for kategori in produk:
        for barang in produk[kategori]["list_barang"]:
            if barang["nama_produk"] == hapus_produk:
                stok_barang = barang['stok']
    selisih = (data_keranjang[hapus_produk]["jumlah"] - jumlah_ubah)
    if ((selisih*-1) > stok_barang) :
        return jsonify({
            "chats": [
                {
                    "text" : "Maaf stok barang kurang",
                    "type" : "text"
                }
            ]
        })
    elif (jumlah_ubah == 0):
        for kategori in produk:
            for barang in produk[kategori]["list_barang"]:
                if barang["nama_produk"] == hapus_produk:
                    barang["stok"] += data_keranjang[hapus_produk]["jumlah"]
        del data_keranjang[hapus_produk]
        return jsonify({
            "chats": [
                {
                    "text" : hapus_produk+" berhasil dihapus dari keranjang!",
                    "type" : "text"
                }
            ]
        })

    else:
        data_keranjang[hapus_produk]["jumlah"] = jumlah_ubah
        for kategori in produk:
            for barang in produk[kategori]["list_barang"]:
                if barang["nama_produk"] == hapus_produk:
                    barang["stok"] += selisih
        return jsonify({
                "chats": [
                    {
                        "text" : "Jumlah "+hapus_produk+" berhasil diubah menjadi "+str(jumlah_ubah)+"!",
                        "type" : "text"
                    }
                ]
            })

@app.route('/keranjang/tambah/<nama>', methods=['POST'])
##contoh bentuk body request {"nama" : "Macbook Air", "harga" : 13000000, "url" : "http://"}
def tambah_keranjang(nama):
    input_produk = { "nama_produk" : request.json['nama'], "harga_produk" : int(request.json['harga']), "url_img" : request.json['url']}
    #I.S Jika stok barang kosong maka tidak akan ditampilkan
    if input_produk["nama_produk"] in data_keranjang :
        data_keranjang[input_produk["nama_produk"]]["jumlah"] += 1
    else:
        data_keranjang[input_produk["nama_produk"]] = {"jumlah": 1, "harga": input_produk["harga_produk"], "url" : input_produk["url_img"]}
    for kategori in produk:
        for barang in produk[kategori]["list_barang"]:
            if barang["nama_produk"] == input_produk["nama_produk"]:
                barang["stok"] -= 1
    return jsonify({"data_keranjang" : data_keranjang})

@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(port=5000)