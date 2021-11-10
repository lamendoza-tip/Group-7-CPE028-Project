package com.example.ortua_app

import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.databinding.DataBindingUtil
import androidx.navigation.findNavController
import com.example.ortua_app.databinding.FragmentLoginBinding
import com.example.ortua_app.databinding.FragmentNotificationsBinding


class NotificationsFragment : Fragment() {

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {

        val binding = DataBindingUtil.inflate<FragmentNotificationsBinding>(
            inflater,
            R.layout.fragment_notifications, container, false
        )

        binding.btnControls.setOnClickListener { view: View ->

            view.findNavController().navigate(R.id.action_notificationsFragment_to_controlsFragment)
        }
        return binding.root
    }

}