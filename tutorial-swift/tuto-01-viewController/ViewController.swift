//
//  ViewController.swift
//  tuto-01-viewController
//
//  Created by Wonyoung Seo on 2021/03/02.
//

import UIKit

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
    }


    @IBAction func sendAlert(_ sender: Any) {
        let alert = UIAlertController(
            title: "Hello",
            message: "My First App",
            preferredStyle: .alert
        )
        let action = UIAlertAction(
            title: "OK",
            style: .default,
            handler: nil
        )
        
        alert.addAction(action)
        present(alert, animated: true, completion: nil)
    }
    
    
}

