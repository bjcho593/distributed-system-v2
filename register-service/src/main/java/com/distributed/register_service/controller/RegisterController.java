package com.distributed.registerservice.controller;

import com.distributed.registerservice.model.User;
import com.distributed.registerservice.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/register")
public class RegisterController {

    @Autowired
    private UserRepository repository;

    @PostMapping
    public String register(@RequestBody User user) {
        if (repository.existsByEmail(user.getEmail())) {
            return "Correo ya registrado";
        }
        repository.save(user);
        return "Usuario registrado exitosamente";
    }
}
