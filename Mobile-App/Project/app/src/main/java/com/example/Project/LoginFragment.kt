package com.example.ortua_app

import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Toast
import androidx.databinding.DataBindingUtil
import androidx.navigation.findNavController
import com.example.ortua_app.databinding.FragmentLoginBinding

class LoginFragment : Fragment() {

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {

        val binding = DataBindingUtil.inflate<FragmentLoginBinding>(inflater,
            R.layout.fragment_login, container, false)

        binding.btnRegacc.setOnClickListener{view : View ->

            view.findNavController().navigate(R.id.action_loginFragment_to_registrationFragment)
        }

        binding.btnLogin.setOnClickListener { view: View ->
            val user = binding.username.text.toString()
            val pass = binding.password.text.toString()
            if ((user == "vyanne") && (pass == "12345")) {
                view.findNavController().navigate(R.id.action_loginFragment_to_homeFragment)
            } else {
                val toast = Toast.makeText(context, "Incorrect Username or Password", Toast.LENGTH_SHORT)
                toast.show()
            }
        }
        return binding.root


    }
}